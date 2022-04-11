import logging
from src.Helpers.Dynamo import DynamoHelper


class SessionRepository:
    def __init__(self):
        self.dbHelper = DynamoHelper()

    def get_session_by_token(self, token: str) -> dict:
        try:
            session = self.dbHelper.get_item_by_key("user_sessions", {"token": token})
            session["id"] = int(session["id"])
            return session
        except Exception as ex:
            logging.error(ex)
            raise ex
