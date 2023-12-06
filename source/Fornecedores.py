import tkinter as tk
from tkinter import messagebox


class CadastroFornecedoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Fornecedores")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_cnpj = tk.Label(root, text="CNPJ:")
        self.label_cnpj.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_cnpj = tk.Entry(root, width=18)
        self.entry_cnpj.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_endereco = tk.Label(root, text="Endereço:")
        self.label_endereco.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_endereco = tk.Entry(root, width=30)
        self.entry_endereco.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_telefone = tk.Label(root, text="Telefone:")
        self.label_telefone.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_telefone = tk.Entry(root, width=15)
        self.entry_telefone.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_fornecedor)
        self.button_cadastrar.grid(row=4, column=0, columnspan=2, pady=20)

    def cadastrar_fornecedor(self):
        nome = self.entry_nome.get()
        cnpj = self.entry_cnpj.get()
        endereco = self.entry_endereco.get()
        telefone = self.entry_telefone.get()

        try:
            # Aqui você pode adicionar lógica para salvar os dados no banco de dados, por exemplo.

            # Exemplo de exibição dos dados (substitua pelo código de armazenamento real):
            mensagem = f"Nome: {nome}\nCNPJ: {cnpj}\nEndereço: {endereco}\nTelefone: {telefone}"

            messagebox.showinfo("Cadastro de Fornecedores", f"Fornecedor cadastrado com sucesso!\n\n{mensagem}")
            self.limpar_campos()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar fornecedor: {e}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cnpj.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroFornecedoresApp(root)
    root.mainloop()
