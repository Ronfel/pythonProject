class ProdutoDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def buscar_produto_por_id(self, produto_id):
        comando_sql = "SELECT * FROM produtos WHERE id = ?"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql, (produto_id,))
        return cursor.fetchone()

    def buscar_todos_os_produtos(self, limite):
        comando_sql = "SELECT * FROM produtos limit ?"
        cursor = self.conexao.cursor()
        cursor.execute(comando_sql, (limite,))
        return cursor.fetchall()