from api import db
from passlib.hash import pbkdf2_sha256

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    pis = db.Column(db.String(20), nullable=False, unique=True)
    pais = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    municipio = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(20), nullable=False)
    rua = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)