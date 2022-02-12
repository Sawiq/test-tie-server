from flask import  request#, jsonify, make_response
from flask_restful import Resource

class AboutResource(Resource):

    def get(self):
        return {
            "version": "0.0.1",
            "name": "Test Tie - test management system"
        }
