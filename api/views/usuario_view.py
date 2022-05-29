from flask_restful import Resource
from api import api
from ..schemas import usuario_schemas
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
from ..paginate import paginate
from ..models.usuario_model import Usuario
from flask_jwt_extended import jwt_required

class UsuarioList(Resource):
    @jwt_required()
    def get(self):
        us = usuario_schemas.UsuarioSchema(many=True)
        return paginate(Usuario, us)

    @jwt_required()
    def post(self):
        us = usuario_schemas.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            pais = request.json["pais"]
            estado = request.json["estado"]
            municipio = request.json["municipio"]
            cep = request.json["cep"]
            rua = request.json["rua"]
            numero = request.json["numero"]
            complemento = request.json["complemento"]
            cpf = request.json["cpf"]
            pis = request.json["pis"]
            senha = request.json["senha"]

            novo_usuario = usuario.Usuario(nome=nome, email=email, pais=pais, estado=estado, municipio=municipio,
                                             cep=cep, rua=rua, numero=numero, complemento=complemento, cpf=cpf,
                                             pis=pis, senha=senha)

            resultado = usuario_service.cadastrar_usuario(novo_usuario)

            return make_response(us.jsonify(resultado), 201)

class UsuariosDetail(Resource):
        @jwt_required()
        def get(self, id):
            usuario = usuario_service.listar_usuario_id(id)
            if usuario is None:
                return make_response(jsonify("UsuarioId não foi encontrado"), 404)
            us = usuario_schemas.UsuarioSchema()
            return make_response(us.jsonify(usuario), 200)

        @jwt_required()
        def put(self, id):
            usuario_db = usuario_service.listar_usuario_id(id)
            if usuario_db is None:
                return make_response(jsonify("UsuarioId não foi encontrado"), 404)
            us = usuario_schemas.UsuarioSchema()
            validate = us.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            else:
                nome = request.json["nome"]
                email = request.json["email"]
                senha = request.json["senha"]
                pais = request.json["pais"]
                estado = request.json["estado"]
                municipio = request.json["municipio"]
                cep = request.json["cep"]
                rua = request.json["rua"]
                numero = request.json["numero"]
                complemento = request.json["complemento"]
                cpf = request.json["cpf"]
                pis = request.json["pis"]

                novo_usuario = usuario.Usuario(nome=nome, email=email, pais=pais, estado=estado,municipio=municipio,
                                                     cep=cep, rua=rua, numero=numero, complemento=complemento, cpf=cpf,
                                                     pis=pis, senha=senha)

                usuario_service.atualiza_usuario(usuario_db, novo_usuario)
                usuario_atualizado = usuario_service.listar_usuario_id(id)

                return make_response(us.jsonify(usuario_atualizado), 200)

        @jwt_required()
        def delete(self, id):
            usuario_db = usuario_service.listar_usuario_id(id)
            if usuario_db is None:
                return make_response(jsonify("UsuarioId não foi encontrado"), 404)
            usuario_service.remove_usuario(usuario_db)
            return make_response(jsonify("Usuario Excluído com Sucesso"), 204)

api.add_resource(UsuarioList, '/usuarios')
api.add_resource(UsuariosDetail, '/usuarios/<int:id>')