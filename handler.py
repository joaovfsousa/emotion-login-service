import json

from src.Helpers.Validator import Validator
from src.Helpers.HttpHelper import HttpHelper


def login(event, context):
    body = json.loads(event["body"])

    if not Validator.is_body_valid(body, ["user", "password"]):
        return HttpHelper.makeError(400, "400-InvalidBody")

    return {"statusCode": 204}
