import secrets

from src.HttpException import HttpException
from src.Repositories.Session import SessionRepository
from src.Repositories.User import UserRepository


class AuthService:
    def __init__(
        self, userRepository: UserRepository, sessionRepository: SessionRepository
    ):
        self.userRepository = userRepository
        self.sessionRepository = sessionRepository

    def authenticate(self, username: str, password: str) -> str:
        user = self.userRepository.get_user_by_username(username)
        if user is None:
            raise HttpException("Usuário não encontrado", "404-UserNotFound", 404)

        if not user.check_password(password):
            raise HttpException(
                "Combinação de usuário e senha não coincide",
                "401-WrongCredentials",
                401,
            )

        token = self.generate_token()

        serializedUser = user.serialize()
        session = {"token": token, **serializedUser}

        self.save_session(session)

        return token

    def save_session(self, session: dict) -> None:
        self.sessionRepository.save_session(session)

    def generate_token(self) -> str:
        return secrets.token_hex(16)
