import tkinter as tk
import source.forms.TelaClientes as TelaClientes
import source.forms.TelaFornecedores as TelaFornecedores
import source.forms.TelaPedidos as TelaPedidos
import source.forms.TelaProdutos as TelaProdutos
import source.reports.RelatorioPedidos as RelatorioPedidos
import source.reports.RelatorioClientes as RelatorioClientes
import source.reports.RelatorioProdutos as RelatorioProdutos
import source.reports.RelatorioFornecedores as RelatorioFornecedores
import source.forms.TelaUsuarios as TelaUsuarios
import source.forms.TelaLogin as TelaLogin


class TelaPrincipalApp:
    def __init__(self, principal):
        self.app = principal
        self.app.title("Tela Principal")

        # Maximizar a tela principal
        self.app.geometry("{0}x{1}+0+0".format(self.app.winfo_screenwidth(), self.app.winfo_screenheight()))

        # Barra de menus
        self.menu_bar = tk.Menu(self.app)
        self.app.config(menu=self.menu_bar)

        # Menu Cadastros
        self.menu_cadastros = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Cadastros", menu=self.menu_cadastros)
        self.menu_cadastros.add_command(label="Clientes", command=self.abrir_cadastro_clientes)
        self.menu_cadastros.add_command(label="Produtos", command=self.abrir_cadastro_produtos)
        self.menu_cadastros.add_command(label="Fornecedores", command=self.abrir_cadastro_fornecedores)
        self.menu_cadastros.add_command(label="Pedidos", command=self.abrir_cadastro_pedidos)

        # Menu Relatórios
        self.menu_relatorios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Relatórios", menu=self.menu_relatorios)
        self.menu_relatorios.add_command(label="Clientes", command=self.abrir_relatorio_clientes)
        self.menu_relatorios.add_command(label="Produtos", command=self.abrir_relatorio_produtos)
        self.menu_relatorios.add_command(label="Pedidos", command=self.abrir_relatorio_pedidos)
        self.menu_relatorios.add_command(label="Fornecedores", command=self.abrir_relatorio_fornecedores)
        # self.menu_cadastros.add_command(label="Pedidos", command=self.abrir_cadastro_pedidos)


        # Menu Relatórios
        self.menu_usuarios = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_command(label="Usuários", command=self.abrir_cadastro_usuarios)

        # Menu Sair
        self.menu_sair = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_command(label="Sair", command=root.destroy)

    def abrir_cadastro_clientes(self):
        dlg = tk.Toplevel(self.app)
        TelaClientes.CadastroClientesApp(dlg)

    def abrir_cadastro_produtos(self):
        dlg = tk.Toplevel(self.app)
        TelaProdutos.CadastroProdutosApp(dlg)

    def abrir_cadastro_fornecedores(self):
        dlg = tk.Toplevel(self.app)
        TelaFornecedores.CadastroFornecedoresApp(dlg)

    def abrir_cadastro_pedidos(self):
        dlg = tk.Toplevel(self.app)
        TelaPedidos.CadastroPedidosApp(dlg)

    def abrir_cadastro_usuarios(self):
        dlg = tk.Toplevel(self.app)
        TelaUsuarios.CadastroUsuariosApp(dlg)

    @staticmethod
    def abrir_relatorio_pedidos():
        RelatorioPedidos.gerar()

    @staticmethod
    def abrir_relatorio_clientes():
        RelatorioClientes.gerar()

    @staticmethod
    def abrir_relatorio_produtos():
        RelatorioProdutos.gerar()

    @staticmethod
    def abrir_relatorio_fornecedores():
        RelatorioFornecedores.gerar()

if __name__ == "__main__":
    root = tk.Tk()
    TelaLogin.TelaLogin(root)
    app = TelaPrincipalApp(root)
    root.mainloop()
