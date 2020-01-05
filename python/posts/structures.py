class UserFeedDataStructure:
    def __init__(self, data: dict = {}):
        self.username = data.get('username', '')
        self.post_message = data.get('post_message', '')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')