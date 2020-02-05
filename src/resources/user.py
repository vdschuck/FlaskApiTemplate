from flask_restful import Resource

class User(Resource):

    def get(self, id):
        return {'user': {}}, 200

    def post(self):
        return {'user': {}}, 201