#!/usr/bin/env python3

"""
TestTie - Test Case Management System
"""

from flask import Flask #, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

#import api.resources as res


app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


db.create_all()

import api.resources
