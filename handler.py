import logging
import json
from src.Repositories.Session import SessionRepository
from src.utils.config_log import config_log
from src.HttpException import HttpException
from src.Services.Auth import AuthService
from src.Repositories.User import UserRepository

from src.Helpers.Validator import Validator
from src.Helpers.Http import HttpHelper

config_log()


def login(event, context):
    try:
        body: dict = json.loads(event["body"])

        if not Validator.is_body_valid(body, ["username", "password"]):
            HttpException("Verifique o corpo da requisição", 400, "400-InvalidBody")

        userRepository = UserRepository()
        sessionRepository = SessionRepository()
        authService = AuthService(userRepository, sessionRepository)

        token = authService.authenticate(body["username"], body["password"])

        return HttpHelper.make_response(200, {"token": token})
    except HttpException as ex:
        return HttpHelper.make_error(ex)
    except Exception as ex:
        logging.error(ex)
        return {"statusCode": 500, "body": json.dumps({"message": "Erro do servidor"})}
