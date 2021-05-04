from app.utilities.exceptions.exceptions import HttpUnauthorized, HttpNotFound


class UserUnauthorized(HttpUnauthorized):
    def __init__(self, message=''):
        HttpUnauthorized.__init__(self, message)


class UserNotFound(HttpNotFound):
    def __init__(self, message=''):
        HttpNotFound.__init__(self, message)

