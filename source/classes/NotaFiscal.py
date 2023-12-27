class NotaFiscal:
    def __init__(self, numero, data_emissao, cliente, produtos):
        self.numero = numero
        self.data_emissao = data_emissao
        self.cliente = cliente
        self.produtos = produtos

    # Métodos getters e setters (conforme necessário)

    def calcular_valor_total(self):
        valor_total = sum(produto.preco * produto.quantidade for produto in self.produtos)
        return valor_total
