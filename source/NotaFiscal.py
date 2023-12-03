from datetime import datetime

class ItemNotaFiscal:
    def __init__(self, descricao, quantidade, preco_unitario):
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def calcular_valor_total(self):
        return self.quantidade * self.preco_unitario

class NotaFiscal:
    def __init__(self, numero, data_emissao, cliente_nome, itens):
        self.numero = numero
        self.data_emissao = data_emissao
        self.cliente_nome = cliente_nome
        self.itens = itens

    def calcular_valor_total(self):
        return sum(item.calcular_valor_total() for item in self.itens)

    def imprimir_nota_fiscal(self):
        print(f"Nota Fiscal #{self.numero}")
        print(f"Data de Emissão: {self.data_emissao.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Cliente: {self.cliente_nome}")
        print("Itens:")
        for i, item in enumerate(self.itens, start=1):
            print(f"  {i}. {item.descricao}: {item.quantidade} x R${item.preco_unitario:.2f} = R${item.calcular_valor_total():.2f}")
        print(f"Valor Total: R${self.calcular_valor_total():.2f}")

# Exemplo de uso:
itens = [
    ItemNotaFiscal("Produto A", 2, 50.0),
    ItemNotaFiscal("Produto B", 1, 30.0),
    ItemNotaFiscal("Produto C", 3, 20.0),
]

data_emissao = datetime.now()

nota_fiscal = NotaFiscal(numero="001/", data_emissao=data_emissao, cliente_nome="Cliente Exemplo", itens=itens)
nota_fiscal.imprimir_nota_fiscal()
