from src.Helpers.Dynamo import DynamoHelper
import logging


class SessionRepository:
    def __init__(self):
        self.db_helper = DynamoHelper()

    def save_session(self, session: dict) -> None:
        try:
            self.db_helper.put_item("user_sessions", session)
        except Exception as ex:
            logging.error(ex)
            raise ex
