import asyncio
from crawler.crawler import TelegramCrawler

from settings import API_ID, API_HASH, TELEGRAM_PRIVATE, SESSION_NAME

KEYWORDS = ['editor.js', 'CodeX']
TELEGRAM_PUBLIC = ['habr_com', 'slaveeks_test_channel', 'test_chat_test_slaveeks']


async def callback(message):
    print(message)


async def main():
    crawler = TelegramCrawler(KEYWORDS, TELEGRAM_PUBLIC, TELEGRAM_PRIVATE, callback, API_ID, API_HASH, SESSION_NAME)

    await crawler.start()


asyncio.run(main())
