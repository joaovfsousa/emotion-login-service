import json

from src.HttpException import HttpException


class HttpHelper:
    @staticmethod
    def makeResponse(statusCode: int, body: dict):
        return {"statusCode": statusCode, "body": json.dumps(body)}

    @staticmethod
    def makeError(exception: HttpException) -> dict:
        exception_as_dict = exception.as_dict()
        return {"statusCode": exception.status, "body": json.dumps(exception_as_dict)}
