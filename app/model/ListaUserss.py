class UserRepo:
    def __init__(self):
        self.list_users = []

    def add_user(self, user: dict):
        self.list_users.insert(0, user)

    def delete_user(self, index: int):
        if 0 <= index < len(self.list_users):
            del self.list_users[index]

    def get_users(self):
        return self.list_users
    
repo = UserRepo()