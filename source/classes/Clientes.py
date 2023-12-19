class Cliente:
    def __init__(self, nome, cpf_cnpj, endereco, email):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco
        self.email = email

    # Métodos getters
    def get_nome(self):
        return self.nome

    def get_cpf_cnpj(self):
        return self.cpf_cnpj

    def get_endereco(self):
        return self.endereco

    def get_email(self):
        return self.email

    # Métodos setters
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_cpf_cnpj(self, novo_cpf_cnpj):
        self.cpf_cnpj = novo_cpf_cnpj

    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def set_email(self, novo_email):
        self.email = novo_email
