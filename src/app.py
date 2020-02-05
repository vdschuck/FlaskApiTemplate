from flask import Flask
from flask_restful import Resource, Api

from src.resources.user import User

# Init app
app = Flask(__name__)
api = Api(app)

# Register resources
api.add_resource(User, '/user', '/user/<id>')