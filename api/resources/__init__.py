from .about import AboutResource
from .user_resources import UserResource
from .user_resources import UsersResource
from api import api

api.add_resource(AboutResource, "/")
api.add_resource(UsersResource, "/users")
api.add_resource(UserResource, "/users/<int:id>")
