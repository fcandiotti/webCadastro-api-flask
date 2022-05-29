class Usuario():
    def __init__(self, nome, cpf, pis, email, senha, pais, estado, municipio, cep, rua, numero, complemento):
        self.__nome = nome
        self.__cpf = cpf
        self.__pis = pis
        self.__email = email
        self.__senha = senha
        self.__pais = pais
        self.__estado = estado
        self.__municipio = municipio
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def pis(self):
        return self.__pis

    @pis.setter
    def pis(self, pis):
        self.__pis = pis

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def municipio(self):
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio):
        self.__municipio = municipio

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, rua):
        self.__rua = rua

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento