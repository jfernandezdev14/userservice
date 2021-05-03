#!flask/bin/python
from flask_restful import Api

from app import app
from app.resources.users_resources import ValidateUsersResource, UsersResource

userservice_api = Api(app)

# List of Endpoints

userservice_api.add_resource(
    ValidateUsersResource,
    '/userservice/api/v1.0/validate-user'
)


userservice_api.add_resource(
    UsersResource,
    '/userservice/api/v1.0/users'
)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)
