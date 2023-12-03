import tkinter as tk
from tkinter import messagebox

class CadastroClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        largura = 280
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

        self.label_email = tk.Label(root, text="E-mail:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_email = tk.Entry(root, width=30)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_cliente)
        self.button_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        if nome and email:
            # Aqui você pode adicionar lógica para salvar os dados no banco de dados, por exemplo.
            messagebox.showinfo("Cadastro de Clientes", "Cliente cadastrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Cadastro de Clientes", "Por favor, preencha todos os campos.")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroClientesApp(root)
    root.mainloop()
