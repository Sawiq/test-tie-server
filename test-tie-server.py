#!/usr/bin/env python3

"""
TestTie - Test Case Management System
"""

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

ma = Marshmallow(app)
api = Api(app)


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(db.String(32))
    role = db.Column(db.String(32))

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return f"<User {self.id}>"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserListResource(Resource):

    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        user = User(**request.json)
        return user_schema.dump(user.create())


class UserResource(Resource):

    def get(self, id):
       user = User.query.get_or_404(id)
       return user_schema.dump(user)


api.add_resource(UserListResource, "/users")
api.add_resource(UserResource, "/users/<int:id>")


db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

