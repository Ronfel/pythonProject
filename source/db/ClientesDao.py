import sqlite3

class ClienteDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def buscar_cliente_por_id(self, cliente_id):
        comando_sql = "SELECT * FROM clientes WHERE id = ?"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql, (cliente_id,))
        return cursor.fetchone()

    def buscar_todos_os_clientes(self):
        comando_sql = "SELECT * FROM clientes"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql)
        return cursor.fetchall()



