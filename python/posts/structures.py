class PostDataStructure:
    def __init__(self, data: dict = {}):
        self.id = data.get('id', '')
        self.user_id = data.get('user_id', '')
        self.username = data.get('username', '')
        self.post = data.get('post', '')
        self.like_count = data.get('like_count', '')
        self.created_at = data.get('created_at', '')
        self.updated_at = data.get('updated_at', '')