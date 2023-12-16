import pyodbc


class ConexaoSQLServer:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            # String de conexão com o SQL Server
            conexao_str = f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"

            # Estabelecer conexão
            self.connection = pyodbc.connect(conexao_str)

            # Criar um objeto cursor para executar consultas SQL
            self.cursor = self.connection.cursor()

            print("Conexão estabelecida com o SQL Server.")

        except Exception as e:
            print(f"Erro ao conectar ao SQL Server: {e}")

    def executar_query(self, query):
        try:
            # Executar a consulta SQL
            self.cursor.execute(query)

            # Commit para aplicar as alterações no banco de dados (quando necessário)
            self.connection.commit()

            print("Consulta executada com sucesso.")

        except Exception as e:
            print(f"Erro ao executar a consulta SQL: {e}")

    def fechar_conexao(self):
        try:
            # Fechar o cursor e a conexão
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

            print("Conexão com o SQL Server fechada.")

        except Exception as e:
            print(f"Erro ao fechar a conexão com o SQL Server: {e}")


# Exemplo de uso:
if __name__ == "__main__":
    # Substitua os valores abaixo pelas suas configurações
    servidor_sql = "seu_servidor_sql"
    banco_dados = "seu_banco_de_dados"
    usuario_sql = "seu_usuario_sql"
    senha_sql = "sua_senha_sql"

    # Criar uma instância da classe de conexão
    conexao_sql = ConexaoSQLServer(servidor_sql, banco_dados, usuario_sql, senha_sql)

    # Conectar ao SQL Server
    conexao_sql.conectar()

    # Exemplo de execução de uma consulta SQL
    consulta_sql = "SELECT * FROM sua_tabela"
    conexao_sql.executar_query(consulta_sql)

    # Fechar a conexão
    conexao_sql.fechar_conexao()
