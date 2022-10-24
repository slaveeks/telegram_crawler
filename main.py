import asyncio
from crawler.crawler import TelegramCrawler

from settings import KEYWORDS, API_ID, API_HASH, TELEGRAM_PUBLIC, TELEGRAM_PRIVATE, SESSION_NAME


async def callback(message):
    print(message)


async def main():
    crawler = TelegramCrawler(KEYWORDS, TELEGRAM_PUBLIC, TELEGRAM_PRIVATE, callback, API_ID, API_HASH, SESSION_NAME)

    await crawler.start()


asyncio.run(main())
