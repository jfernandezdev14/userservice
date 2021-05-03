from flask import request, jsonify
from flask_restful import Resource

from app.controllers.users_controller import UsersController
from app.utilities.decorators.decorators import api_resource_endpoint


class UsersResource(Resource):
    """
    Contains the list of methods exposed of the UsersResource
    """
    def get(self):
        """
        Retrieves the information of an user
        :return:
        """
        users_controller = UsersController()
        users = users_controller.retrieve_all_users()
        print(users)
        return jsonify(users)


class ValidateUsersResource(Resource):
    """
    Contains the list of endpoints exposed of the ValidateUsersResource
    """
    @api_resource_endpoint()
    def get(self):
        """
        Validates if the information given of an specific user is valid
        :return: Dict, Contains a json response specifying if the information of the user is valid,
         otherwise an exception is raised. Ie, {'is_valid': True}
        """
        data = request.get_json(force=True)
        users_controller = UsersController()
        user = users_controller.validate_user_account(user_data=data)
        return jsonify(user)
