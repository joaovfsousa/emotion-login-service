from src.Helpers.Hash import HashHelper


class User:
    def __init__(self, id, name, username, password):
        self.username = username
        self.password = password
        self.name = name
        self.id = id

    def checkPassword(self, password: str) -> bool:
        passwordHash = HashHelper.hash_string(password)
        return passwordHash == self.password
