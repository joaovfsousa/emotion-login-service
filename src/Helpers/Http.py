import json

from src.HttpException import HttpException


class HttpHelper:
    @staticmethod
    def make_response(statusCode: int, body: dict):
        return {"statusCode": statusCode, "body": json.dumps(body)}

    @staticmethod
    def make_error(exception: HttpException) -> dict:
        exception_as_dict = exception.as_dict()
        return {"statusCode": exception.status, "body": json.dumps(exception_as_dict)}
