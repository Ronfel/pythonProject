import tkinter as tk
from tkinter import messagebox
import source.classes.Usuarios as user

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de Login")

        # Labels e Entradas para Nome de Usuário e Senha
        self.label_usuario = tk.Label(root, text="Nome de Usuário:")
        self.label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_usuario = tk.Entry(root, width=30)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_senha = tk.Entry(root, show="*", width=30)  # A opção show="*" oculta a senha
        self.entry_senha.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Botão de Login
        self.button_login = tk.Button(root, text="Login", command=self.realizar_login)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=20)

    def realizar_login(self):
        # Obter nome de usuário e senha inseridos
        user.login = self.entry_usuario.get()
        user.senha = self.entry_senha.get()

        # Exemplo de verificação de credenciais (substitua por lógica de login real)
        if user.login == "Rodrigo" and user.senha == "123":
            messagebox.showinfo("Login", "Login bem-sucedido!")
            # Adicione aqui a lógica para abrir a próxima tela ou realizar outras ações pós-login
            return True
        else:
            messagebox.showerror("Login", "Nome de usuário ou senha incorretos. Tente novamente.")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()
