class SignUpStructure:
    def __init__(self, data: dict = {}):
        self.username = data.get('username', '')
        self.email = data.get('email', '')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        self.password = data.get('password', '')
        self.password_confirm = data.get('password_confirm', '')

class SignInStructure:
    def __init__(self, data: dict = {}):
        self.username = data.get('username', '')
        self.password = data.get('password', '')