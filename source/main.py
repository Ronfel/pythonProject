import tkinter as tk
import Clientes
import Fornecedores
import Pedidos
import Produtos
import RelatorioPedidos

class TelaPrincipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")

        # Maximizar a tela principal
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        # Barra de menus
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Menu Cadastros
        self.menu_cadastros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cadastros", menu=self.menu_cadastros)
        self.menu_cadastros.add_command(label="Clientes", command=self.abrir_cadastro_clientes)
        self.menu_cadastros.add_command(label="Produtos", command=self.abrir_cadastro_produtos)
        self.menu_cadastros.add_command(label="Fornecedores", command=self.abrir_cadastro_fornecedores)
        self.menu_cadastros.add_command(label="Pedidos", command=self.abrir_cadastro_pedidos)
        self.menu_cadastros.add_separator()
        self.menu_cadastros.add_command(label="Sair", command=root.destroy)

        # Menu Relatórios
        self.menu_relatorios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Relatórios", menu=self.menu_relatorios)
        self.menu_relatorios.add_command(label="Pedidos", command=self.abrir_relatorio_pedidos)

    def abrir_cadastro_clientes(self):
        root = tk.Toplevel(self.root)
        app = Clientes.CadastroClientesApp(root)

    def abrir_cadastro_produtos(self):
        root = tk.Toplevel(self.root)
        app = Produtos.CadastroProdutosApp(root)

    def abrir_cadastro_fornecedores(self):
        root = tk.Toplevel(self.root)
        app =  Fornecedores.CadastroFornecedoresApp(root)

    def abrir_cadastro_pedidos(self):
        root = tk.Toplevel(self.root)
        app =  Fornecedores.CadastroPedidosApp(root)

    def abrir_relatorio_pedidos(self):
        RelatorioPedidos.gerar()

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipalApp(root)
    root.mainloop()
