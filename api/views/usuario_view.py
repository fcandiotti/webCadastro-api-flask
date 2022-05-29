from flask_restful import Resource
from api import api

class UsuarioList(Resource):
    def get(self):
        return "Ola"

api.add_resource(UsuarioList, '/usuarios')