import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.', '.env')
load_dotenv(dotenv_path)

TELEGRAM_PUBLIC = os.environ.get('TELEGRAM_PUBLIC')

TELEGRAM_PRIVATE = os.environ.get('TELEGRAM_PRIVATE')

API_ID = int(os.environ.get('API_ID'))

API_HASH = os.environ.get('API_HASH')

SESSION_NAME = os.environ.get('SESSION_NAME')

KEYWORDS = os.environ.get('KEYWORDS')
