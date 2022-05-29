from api.models import usuario_model
from api import db

def cadastrar_usuario(usuario):

    usuario_db = usuario_model.Usuario(nome=usuario.nome, cpf=usuario.cpf, pis=usuario.pis,
                                          email=usuario.email, senha=usuario.senha, pais=usuario.pais,
                                          estado=usuario.estado, municipio=usuario.municipio, cep=usuario.cep,
                                          rua=usuario.rua, numero=usuario.numero, complemento=usuario.complemento)
    usuario_db.encriptar_senha()
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def listar_usuarios():
    usuarios = usuario_model.Usuario.query.all()
    return usuarios

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario

def atualiza_usuari(usuario_db, novo_usuario):
    usuario_db.nome = novo_usuario.nome
    usuario_db.cpf = novo_usuario.cpf
    usuario_db.pis = novo_usuario.pis
    usuario_db.email = novo_usuario.email
    usuario_db.pais = novo_usuario.pais
    usuario_db.estado = novo_usuario.estado
    usuario_db.municipio = novo_usuario.municipio
    usuario_db.cep = novo_usuario.cep
    usuario_db.rua = novo_usuario.rua
    usuario_db.numero = novo_usuario.numero
    usuario_db.complemento = novo_usuario.complemento
    db.session.commit()

def remove_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()

def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()