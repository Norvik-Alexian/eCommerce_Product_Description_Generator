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

        first_description = model['choices'][0]['text']
        second_description = model['choices'][1]['text']

        return first_description, second_description


output = ProductDescription()
print(output.generate_description(['Ucraft', 'e-commerce', 'website builder']))