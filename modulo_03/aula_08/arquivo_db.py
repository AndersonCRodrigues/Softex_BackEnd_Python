import sqlite3


class ConexaoDB:
    """Gerencia a conexão bruta com o SQLite."""

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self._criar_tabela()

    def _criar_tabela(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas(
            id INTEGER PRIMARY KEY,
            descricao TEXT,
            concluida INTEGER
            )"""
        )
        self.conn.commit()

    def obter_conexao(self):
        return self.conn

    def fechar(self):
        self.conn.close()


class GerenciadorTarefas:
    """Gerencia a lógica de negócio, usando a ConexaoDB."""

    def __init__(self, db_conn: ConexaoDB):  # <--- INJEÇÃO DE DEPENDÊNCIA
        self.db_conn = db_conn
        self.conn = db_conn.obter_conexao()

    def adicionar_tarefa(self, descricao: str):
        self.conn.execute(
            "INSERT INTO tarefas (descricao, concluida) VALUES (?, 0)", (descricao,)
        )
        self.conn.commit()

    def contar_tarefas(self) -> int:
        cursor = self.conn.cursor()
        resultado = cursor.execute("SELECT COUNT(*) FROM tarefas").fetchone()
        return resultado[0]


# conn = ConexaoDB("banco.db")
# gerente = GerenciadorTarefas(conn)
# gerente.adicionar_tarefa("tarefa de uso de desenvolvimento/produção")
# print(gerente.contar_tarefas())
