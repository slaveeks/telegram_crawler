from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty


class Group:
    """
    The Telegram Group
    :param channel - telegram channel entity
    :param client - telegram client
    :param title - channel title
    :param group_id - channel id
    """

    def __init__(self, channel, client, title, group_id):
        self.channel = channel
        self.client = client
        self.title = title
        self.group_id = group_id

    @staticmethod
    async def get_group_by_data(data, client):
        """
        Get Group object by data
        :param data - data for finding
        :param client - telegram client
        :returns - Group instance
        """
        channel = await client.get_entity(data)
        return Group(channel, client, channel.title, channel.id)

    async def join_to_group(self):
        """
        join to telegram group
        """
        await self.client(JoinChannelRequest(self.channel))

    async def search_messages(self, keywords):
        """
        Search messages with keywords in telegram channel
        :param keywords - keywords for searching
        """
        search_filter = InputMessagesFilterEmpty()
        result = []
        for keyword in keywords:
            data = await self.client(SearchRequest(self.channel, q=keyword, filter=search_filter, min_date=None,
                                                   max_date=None,
                                                   offset_id=0,
                                                   add_offset=0,
                                                   limit=10000,
                                                   max_id=0,
                                                   min_id=0,
                                                   from_id=None,
                                                   hash=0))
            for message in data.messages:
                result.append(message)
        return result
