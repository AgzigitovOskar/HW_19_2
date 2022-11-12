from dao.model.user import UserSchema
from flask import request
from flask_restx import Namespace, Resource
from implemented import user_service

# создание нового namespace
user_ns = Namespace('/users')

# создание схем для  User
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def post(self):
        """
            создание нового user
        """
        req_json = request.json
        user_service.create(req_json)

        return '', 201


