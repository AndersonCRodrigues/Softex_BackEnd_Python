import sqlite3


class DatabaseConnection:
    """Gerencia a conexão com o banco de dados SQLite."""

    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Abre a conexão com o banco de dados."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None
