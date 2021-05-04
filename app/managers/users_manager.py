from bson.json_util import dumps

from app import db


class UsersManager(object):
    """"
    Contains methods to access or store data of the Users
    """

    def __init__(self):
        """
        Initializes UsersManager instance setting a database session
        """
        self.__db_session = db

    def create_user(self, user_data):
        """"
        Creates an user with its user_id and pin
        """
        self.__db_session.users.insert_one(
            {
             "user_id": user_data.get("user_id"),
             "pin": user_data.get("pin"),
            }
        )

    def retrieve_user(self, user_data):
        """"
        Creates an user with its user_id and pin
        :param user_data: Dict, contains the information of the user to retrieve. Ie, {"user_id": "user123"}
        :return: Dict,
        """
        user = self.__db_session.users.find_one(user_data)
        return user

    def retrieve_all_users(self):
        users = self.__db_session.users.find()
        if users:
            users = [{'user_id': user['user_id'], 'pin': user['pin']} for user in users]
        return users

    def update_user(self):
        pass

    def delete_user(self):
        pass
