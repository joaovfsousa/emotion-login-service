import json


class HttpHelper:
    @staticmethod
    def makeResponse(statusCode, body):
        return {"statusCode": statusCode, "body": json.dumps(body)}

    @staticmethod
    def makeError(statusCode, errorCode):
        return {"statusCode": statusCode, "body": json.dumps({"errorCode": errorCode})}
