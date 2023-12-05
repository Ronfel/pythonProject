import tkinter as tk
from tkinter import messagebox

class CadastroProdutosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")

        largura = 290
        altura = 150

        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()

        x = (largura_tela / 2) - (largura / 2)
        y = (altura_tela / 2) - (altura / 2)

        self.root.geometry(f'{largura}x{altura}+{int(x)}+{int(y)}')

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_descricao = tk.Label(root, text="Descrição:")
        self.label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_descricao = tk.Entry(root, width=30)
        self.entry_descricao.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_preco = tk.Label(root, text="Preço:")
        self.label_preco.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_preco = tk.Entry(root, width=10)
        self.entry_preco.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_produto)
        self.button_cadastrar.grid(row=3, column=0, columnspan=2, pady=20)

    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        preco = self.entry_preco.get()

        try:
            # Converte o preço para float
            preco = float(preco)

            # Aqui você pode adicionar lógica para salvar os dados no banco de dados, por exemplo.

            messagebox.showinfo("Cadastro de Produtos", "Produto cadastrado com sucesso!")
            self.limpar_campos()

        except ValueError:
            messagebox.showwarning("Cadastro de Produtos", "Por favor, insira um preço válido.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroProdutosApp(root)
    root.mainloop()
