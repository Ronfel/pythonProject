class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, codigo_produto, quantidade_adicionar):
        for produto in self.produtos:
            if produto.get_codigo() == codigo_produto:
                nova_quantidade = produto.get_quantidade_estoque() + quantidade_adicionar
                produto.set_quantidade_estoque(nova_quantidade)
                break
        else:
            print(f"Produto com código {codigo_produto} não encontrado.")

    def remover_produto(self, codigo_produto, quantidade_remover):
        for produto in self.produtos:
            if produto.get_codigo() == codigo_produto:
                nova_quantidade = produto.get_quantidade_estoque() - quantidade_remover
                if nova_quantidade >= 0:
                    produto.set_quantidade_estoque(nova_quantidade)
                else:
                    print("Quantidade a ser removida é maior que a quantidade em estoque.")
                break
        else:
            print(f"Produto com código {codigo_produto} não encontrado.")

    def obter_info_estoque(self):
        info_estoque = []
        for produto in self.produtos:
            info_produto = {
                "Nome": produto.get_nome(),
                "Código": produto.get_codigo(),
                "Preço": produto.get_preco(),
                "Quantidade em Estoque": produto.get_quantidade_estoque(),
                "Quantidade Mínima": produto.get_quantidade_minima(),
                "Quantidade Máxima": produto.get_quantidade_maxima(),
            }
            info_estoque.append(info_produto)
        return info_estoque

