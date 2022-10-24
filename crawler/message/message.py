from telethon.tl.functions.messages import GetRepliesRequest


class Message:
    """
    The Telegram Message
    :param message_data - incoming data from telegram
    """

    def __init__(self, message_data):
        self.text = message_data.message
        self.comments = []
        self.message_id = message_data.id
        self.group_id = message_data.peer_id
        self.date = message_data.date

    async def get_replies(self, client):
        """
        Get replies to message
        :param client - telegram client
        """
        try:
            messages = await client(GetRepliesRequest(msg_id=self.message_id, offset_id=0, add_offset=0, limit=100000,
                                                      max_id=0,
                                                      min_id=0,
                                                      hash=0,
                                                      peer=self.group_id,
                                                      offset_date=None))
            for message in messages.messages:
                self.comments.append(Message(message))
        except (Exception,):
            print('No comments')

    def search_by_keywords(self, keywords):
        """
        Check is message consists keywords
        :param keywords - keywords to find
        :returns - true, if keyword was found
        """
        for keyword in keywords:
            if keyword in self.text:
                return True
        return False
