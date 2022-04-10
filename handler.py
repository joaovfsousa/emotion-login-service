import json
import logging
from src.HttpException import HttpException
from src.Services.Auth import AuthService
from src.Repositories.User import UserRepository

from src.Helpers.Validator import Validator
from src.Helpers.Http import HttpHelper


def login(event, context):
    try:
        body: dict = json.loads(event["body"])

        if not Validator.is_body_valid(body, ["username", "password"]):
            HttpException("Verifique o corpo da requisição", 400, "400-InvalidBody")

        userRepository = UserRepository()
        authService = AuthService(userRepository)

        token = authService.authenticate(body["username"], body["password"])

        return HttpHelper.makeResponse(200, {"token": token})
    except HttpException as ex:
        return HttpHelper.makeError(ex)
    except Exception as ex:
        logging.error(ex)
        return {"statusCode": 500, "body": json.dumps({"message": "Erro do servidor"})}
