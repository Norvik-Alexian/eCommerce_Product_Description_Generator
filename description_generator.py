import os
import openai
import config

from dotenv import load_dotenv

load_dotenv()
OPENAI_SECRET_API_KEY = os.getenv('OPENAI_SECRET_API_KEY')

if not OPENAI_SECRET_API_KEY:
    raise EnvironmentError('You should set OPENAI_SECRET_API_KEY as your environment variable.')


class ProductDescription:
    openai.api_key = OPENAI_SECRET_API_KEY

    def __init__(self,
                 engine=config.ENGINE,
                 max_tokens=config.MAX_TOKENS,
                 top_p=config.TOP_P,
                 frequency_penalty=config.FREQUENCY_PENALTY,
                 presence_penalty=config.PRESENCE_PENALTY):
        self.engine = engine
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    @staticmethod
    def prettifier(content: str, finish_reason: str):
        if finish_reason == 'length':
            ending_punctuations = config.ENDING_PUNCTUATION
            any_finished_sequence = any([mark in content for mark in ending_punctuations])
            if any_finished_sequence:
                reversed_content = content[::-1]
                last_finished_sequence = len(content) - 1 - min(
                    [reversed_content.index(mark) for mark in ending_punctuations if mark in content]
                )
                content = content[:last_finished_sequence+1]

        content = config.REMOVE_EXTRA_SPACE_PATTERN.sub(' ', content)

        return content

    def generate_description(self, keywords: list):
        model = openai.Completion.create(
            engine=self.engine,
            prompt=f'Generate Product Description within Keywords\nKeywords: {keywords}\nProduct Description:',
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            n=2
        )

        first_description = model['choices'][0]['text'].strip()
        first_finish_reason = model['choices'][0]['finish_reason']

        second_description = model['choices'][1]['text'].strip()
        second_finish_reason = model['choices'][1]['finish_reason']

        return self.prettifier(first_description, first_finish_reason), self.prettifier(second_description, second_finish_reason)

    def generate_highlight(self, keywords: list):
        first_description, second_description = self.generate_description(keywords)
        model = openai.Completion.create(
            engine=config.ENGINE,
            prompt=f'{config.HIGHLIGHT_PROMPT}\n\nProduct Description: {second_description}\nHighlights:',
            max_tokens=config.MAX_TOKENS,
            top_p=config.TOP_P,
            frequency_penalty=config.FREQUENCY_PENALTY,
            presence_penalty=config.PRESENCE_PENALTY
        )

        description_highlight_format = f'{first_description}\n\nHighlights:\n{model["choices"][0]["text"].strip()}'

        return description_highlight_format
