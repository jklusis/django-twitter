class UserSettingStructure:
    def __init__(self, data: dict = {}):
        self.username = data.get('username', '')
        self.email = data.get('email', '')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        self.password_current = data.get('password_current', '')
        self.password_new = data.get('password_new', '')
        self.password_new_confirm = data.get('password_new_confirm', '')

class UserDataStructure:
    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.first_name = None
        self.last_name = None
        self.date_joined = None
        self.following_count = None
        self.follower_count = None
        self.post_count = None
    