import tkinter as tk
from tkinter import messagebox


class CadastroUsuariosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuários")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_nome = tk.Entry(root, width=30)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_email = tk.Label(root, text="E-mail:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_email = tk.Entry(root, width=30)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_senha = tk.Entry(root, width=15, show="*")  # A opção show="*" oculta a senha
        self.entry_senha.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.button_cadastrar.grid(row=3, column=0, columnspan=2, pady=20)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        try:
            # Aqui você pode adicionar lógica para salvar os dados no banco de dados, por exemplo.

            # Exemplo de exibição dos dados (substitua pelo código de armazenamento real):
            mensagem = f"Nome: {nome}\nE-mail: {email}\nSenha: {senha}"

            messagebox.showinfo("Cadastro de Usuários", f"Usuário cadastrado com sucesso!\n\n{mensagem}")
            self.limpar_campos()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroUsuariosApp(root)
    root.mainloop()
