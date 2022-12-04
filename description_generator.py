import os
import openai

from dotenv import load_dotenv

load_dotenv()
OPENAI_SECRET_API_KEY = os.getenv('OPENAI_SECRET_API_KEY')

if not OPENAI_SECRET_API_KEY:
    raise EnvironmentError('You should set OPENAI_SECRET_API_KEY as your environment variable.')
