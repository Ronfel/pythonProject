# classes/usuario.py

class Usuario:
    def __init__(self, login, senha, email):
        self.login = login
        self.senha = senha
        self.email = email

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, login):
        self.login = login

    @property
    def senha(self):
        return self.senha

    @senha.setter
    def senha(self, senha):
        self.senha = senha