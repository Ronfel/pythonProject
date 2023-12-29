import sqlite3

class FornecedorDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def buscar_fornecedor_por_id(self, fornecedor_id):
        comando_sql = "SELECT * FROM fornecedores WHERE id = ?"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql, (fornecedor_id,))
        return cursor.fetchone()

    def buscar_todos_os_fornecedores(self):
        comando_sql = "SELECT * FROM fornecedores"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql)
        return cursor.fetchall()
