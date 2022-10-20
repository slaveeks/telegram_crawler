from telethon.tl.functions.messages import SearchRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import events
from telethon.tl.types import InputMessagesFilterEmpty
from telethon import TelegramClient

SESSION_NAME = 'my_session'

api_id = ''
api_hash = ''


class TelegramCrawler:
    """
    The TelegramCrawler gets data from telegram
    :param client - telethon client
    :param keywords - words to find
    :param telegram_public - telegram public channels or chats
    :param callback - function to handle found information
    """

    def __init__(self, keywords, telegram_public, telegram_private, callback):
        self.client = None
        self.callback = callback
        self.channels = []
        self.keywords = keywords
        self.telegram_public = telegram_public
        self.telegram_private = telegram_private

    async def start(self):
        """
        Initiating Telegram Client and starting crawling
        """
        async with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
            self.client = client
            await self.__prepare_crawling()
            await self.__start_crawling()

    async def __prepare_crawling(self):
        """
        Joining to public channels and get its entities
        """
        for channel in self.telegram_public:
            channel_entity = await self.client.get_entity(channel)
            await self.client(JoinChannelRequest(channel_entity))
            self.channels.append(channel_entity)

    async def __start_crawling(self):
        """
        Make first search in public channels and chats
        """

        # Create empty filter for search
        search_filter = InputMessagesFilterEmpty()

        # Take a look in the list of saved channels
        for channel in self.channels:
            # Make a search in channel for every keyword
            for keyword in self.keywords:
                data = await self.client(SearchRequest(channel, q=keyword, filter=search_filter,
                                                       min_date=None,
                                                       max_date=None,
                                                       offset_id=0,
                                                       add_offset=0,
                                                       limit=100000,
                                                       max_id=0,
                                                       min_id=0,
                                                       from_id=None,
                                                       hash=0))

                # Parse found messages
                for message in data.messages:
                    await self.__parse_message(message, channel.title, channel.id)

        # Create handler for incoming messages
        @self.client.on(events.NewMessage)
        async def handler(event):
            """
            For incoming events calls parsing events function
            :param event: incoming telegram event
            """
            await self.__parse_event(event.original_update.message)

        # Run telegram client to wait for incoming events
        await self.client.run_until_disconnected()

    async def __parse_event(self, data):
        """
        Checks for keywords incoming messages
        :param data: incoming telegram message object
        """
        entity = await self.client.get_entity(data.peer_id)
        for keyword in self.keywords:
            if keyword in data.message:
                await self.__parse_message(data, entity.title, entity.id)
                break

    async def __parse_message(self, message, source_name, source_id):
        """
        Create object for callback function and call it
        :param message: message to parse
        """
        data = {
            'title': message.message,
            'date': message.date,
            'author': source_name,
        }

        await self.callback(data)