import asyncio
from crawler.crawler import TelegramCrawler
import requests

keywords = ['editor.js', 'CodeX']

telegram_public = ['']

telegram_private = []

api_id = ''
api_hash = ''

session_name = 'my_session'


async def callback(message):
    requests.post('https://notify.bot.codex.so/u/', data={
        'message': str(message),
    })


async def main():
    crawler = TelegramCrawler(keywords, telegram_public, telegram_private, callback, api_id, api_hash, session_name)

    await crawler.start()


asyncio.run(main())
