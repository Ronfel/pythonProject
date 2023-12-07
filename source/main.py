import tkinter as tk
import Clientes
import Fornecedores
import Pedidos
import Produtos

class TelaPrincipalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Principal")

        # Barra de menus
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        # Menu Cadastros
        self.menu_cadastros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cadastros", menu=self.menu_cadastros)
        self.menu_cadastros.add_command(label="Clientes", command=self.abrir_cadastro_clientes)
        self.menu_cadastros.add_command(label="Produtos", command=self.abrir_cadastro_produtos)
        self.menu_cadastros.add_command(label="Fornecedores", command=self.abrir_cadastro_fornecedores)
        self.menu_cadastros.add_separator()
        self.menu_cadastros.add_command(label="Sair", command=root.destroy)

    def abrir_cadastro_clientes(self):
        root = tk.Toplevel(self.root)
        app = Clientes.CadastroClientesApp(root)

    def abrir_cadastro_produtos(self):
        root = tk.Toplevel(self.root)
        app = Produtos.CadastroProdutosApp(root)

    def abrir_cadastro_fornecedores(self):
        root = tk.Toplevel(self.root)
        app =  Fornecedores.CadastroFornecedoresApp(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaPrincipalApp(root)
    root.mainloop()
