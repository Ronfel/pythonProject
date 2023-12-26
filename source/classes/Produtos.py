class Produto:
    def __init__(self, nome, codigo, preco, quantidade_estoque):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade_estoque

    # Métodos getters
    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo

    def get_preco(self):
        return self.preco

    def get_quantidade_estoque(self):
        return self.quantidade_estoque

    # Métodos setters
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo

    def set_preco(self, novo_preco):
        self.preco = novo_preco

