from app.DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException


class UserSession(object):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance

    def get_logged_user(self):
        raise DependendClassCallDuringUnitTestException(
            "UserSession.getLoggedUser() should not be called in an unit test"
        )
