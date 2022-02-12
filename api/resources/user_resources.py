from flask import  request#, jsonify, make_response
from flask_restful import Resource

from api.models import User
import api.schemas

class UserResource(Resource):

    def get(self, id):
       user = User.query.get_or_404(id)
       return api.schemas.user.dump(user)

    def put(self, id):
       user = User.query.get_or_404(id)
       user_schema


class UsersResource(Resource):

    def get(self):
        users = User.query.all()
        return api.schemas.users.dump(users)

    def post(self):
        user = User(**request.json)
        return api.schemas.user.dump(user.create())

