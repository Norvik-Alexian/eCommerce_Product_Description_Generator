import os
import openai

from dotenv import load_dotenv

load_dotenv()
OPENAI_SECRET_API_KEY = os.getenv('OPENAI_SECRET_API_KEY')

if not OPENAI_SECRET_API_KEY:
    raise EnvironmentError('You should set OPENAI_SECRET_API_KEY as your environment variable.')


def generate_description(keywords: list):
    openai.api_key = OPENAI_SECRET_API_KEY
    model = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'Generate Product Description within Keywords\nKeywords: {keywords}\nProduct Description:',
        max_tokens=80,
        top_p=1.,
        frequency_penalty=1.,
        presence_penalty=1.,
        n=2
    )

    return model


print(generate_description(['Ucraft', 'e-commerce', 'website builder']))