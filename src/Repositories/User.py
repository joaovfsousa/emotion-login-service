from src.HttpException import HttpException
from src.Models.User import User
from src.Helpers.MySQL import MySQLHelper
import logging


class UserRepository:
    def __init__(self):
        self.dbHelper = MySQLHelper()

    def get_user_by_username(self, username: str) -> User:
        try:
            cursor = self.dbHelper.getCursor()
            query = (
                "SELECT id, name, username, password FROM users u where u.username = %s"
            )
            cursor.execute(query, username)

            line = cursor.fetchone()

            if line is None:
                return None

            id, name, username, password = line

            user = User(id, name, username, password)
            return user

        except Exception as ex:
            logging.error(ex)
            raise HttpException(
                "Erro ao buscar usuário no banco", 500, "500-InternalServerError"
            )
