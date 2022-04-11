import json
import logging

from src.Helpers.Http import HttpHelper
from src.HttpException import HttpException
from src.Repositories.Session import SessionRepository
from src.Services.Session import SessionService
from src.utils.config_log import config_log

config_log()


def get_session(event, context):
    try:
        token = event["headers"].get("authorization")

        if token is None:
            raise HttpException(
                "Header de autorização faltando", "401-NotAuthorized", 401
            )

        session_repository = SessionRepository()
        session_service = SessionService(session_repository)

        item = session_service.get_session_by_token(token)

        if item is None:
            raise HttpException("Sessão não encontrada", "401-NotAuthorized", 401)

        return HttpHelper.makeResponse(200, item)
    except HttpException as ex:
        return HttpHelper.makeError(ex)
    except Exception as ex:
        logging.error(ex)
        return {"statusCode": 500, "body": json.dumps({"message": "Erro do servidor"})}
