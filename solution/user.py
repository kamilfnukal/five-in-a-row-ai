import pickle
import string


class User:
    def __init__(self, user_nickname: string, user_email: string, user_id: string, user_token: string):
        self.nickname = user_nickname
        self.email = user_email
        self.id = user_id
        self.token = user_token

    def save_user(self):
        with open(f'./users/{self.nickname}.txt', 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_user(user_nickname) -> 'User':
        with open(f'./users/{user_nickname}.txt', 'rb') as file:
            loaded_user = pickle.load(file)
        return loaded_user
