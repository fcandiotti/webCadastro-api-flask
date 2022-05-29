from api import ma
from ..models import usuario_model
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario
        load_instance = True
        fields = ('id', 'nome', 'cpf', 'pis', 'email', 'senha', 'pais', 'estado', 'municipio', 'cep', 'rua', 'numero',
                  'complemento')

    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    pis = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    pais = fields.String(required=True)
    estado = fields.String(required=True)
    municipio = fields.String(required=True)
    cep = fields.String(required=True)
    rua = fields.String(required=True)
    numero = fields.Integer(required=True)
    complemento = fields.String(required=True)