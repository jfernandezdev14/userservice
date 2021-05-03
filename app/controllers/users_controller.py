from app.utilities.exceptions.users_exceptions import UserUnauthorized, UserNotFound
from app.managers.users_manager import UsersManager


class UsersController(object):
    """
    Contains the logic related to the users functionalities
    """

    @staticmethod
    def validate_user_account(user_data):
        """
        Validates if the user data received matches with an existing user
        :param user_data: Dict, Contains the user information. Ie, {"user_id": "user123", "pin": "pass123"}
        :return: Dict, Returns the information of the user validated
        """

        user_manager = UsersManager()
        user_retrieved = user_manager.retrieve_user({"user_id": user_data.get("user_id")})
        if not user_retrieved:
            raise UserNotFound(message="The user given doesn't exists, please confirm if the values are correct")
        if user_retrieved['pin'] != user_data.get("pin"):
            raise UserUnauthorized(message="Password incorrect or not valid")
        user = {'user_id': user_retrieved['user_id']}
        return user

    @staticmethod
    def retrieve_all_users():
        """
        Validates if the user data received matches with an existing user
        :return: List, List of users
        """

        user_manager = UsersManager()
        users_retrieved = user_manager.retrieve_all_users()
        return users_retrieved
