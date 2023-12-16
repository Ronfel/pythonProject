import tkinter as tk
from tkinter import messagebox

class CadastroPedidosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Pedidos")

        self.label_cliente = tk.Label(root, text="Cliente:")
        self.label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_cliente = tk.Entry(root, width=30)
        self.entry_cliente.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_produto = tk.Label(root, text="Produto:")
        self.label_produto.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_produto = tk.Entry(root, width=30)
        self.entry_produto.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_quantidade = tk.Label(root, text="Quantidade:")
        self.label_quantidade.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_quantidade = tk.Entry(root, width=10)
        self.entry_quantidade.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.button_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_pedido)
        self.button_cadastrar.grid(row=3, column=0, columnspan=2, pady=20)

    def cadastrar_pedido(self):
        cliente = self.entry_cliente.get()
        produto = self.entry_produto.get()
        quantidade = self.entry_quantidade.get()

        try:
            # Converte a quantidade para int
            quantidade = int(quantidade)

            # Aqui você pode adicionar lógica para salvar os dados no banco de dados, por exemplo.

            messagebox.showinfo("Cadastro de Pedidos", "Pedido cadastrado com sucesso!")
            self.limpar_campos()

        except ValueError:
            messagebox.showwarning("Cadastro de Pedidos", "Por favor, insira uma quantidade válida.")

    def limpar_campos(self):
        self.entry_cliente.delete(0, tk.END)
        self.entry_produto.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroPedidosApp(root)
    root.mainloop()
