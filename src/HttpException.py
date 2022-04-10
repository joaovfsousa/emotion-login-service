import logging


class HttpException(Exception):
    def __init__(self, message: str, code: str, status: int):
        super().__init__(self, message)
        self.message = message
        self.code = code
        self.status = status

    def as_dict(self):
        exception_as_dict = {
            "code": self.code,
            "message": self.message,
        }
        logging.warn(exception_as_dict)
        return exception_as_dict
