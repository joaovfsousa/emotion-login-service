from src.Helpers.Hash import HashHelper


class User:
    def __init__(self, id, name, username, password):
        self.username = username
        self.password = password
        self.name = name
        self.id = id

    def check_password(self, password: str) -> bool:
        passwordHash = HashHelper.hash_string(password)
        return passwordHash == self.password

    def serialize(self) -> dict:
        return {"username": self.username, "name": self.name, "id": self.id}
