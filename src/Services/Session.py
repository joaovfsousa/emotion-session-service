from src.Repositories.Session import SessionRepository


class SessionService:
    def __init__(self, sessionRepository: SessionRepository):
        self.sessionRepository = sessionRepository

    def get_session_by_token(self, token: str):
        return self.sessionRepository.get_session_by_token(token)
