import secrets
from src.HttpException import HttpException
from src.Repositories.User import UserRepository


class AuthService:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def authenticate(self, username: str, password: str) -> str:
        user = self.userRepository.getUserByUsername(username)
        if user is None:
            raise HttpException("Usuário não encontrado", "404-UserNotFound", 404)

        if not user.checkPassword(password):
            raise HttpException(
                "Combinação de usuário e senha não coincide",
                "401-WrongCredentials",
                401,
            )

        token = secrets.token_hex(16)

        return token