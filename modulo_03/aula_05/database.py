import sqlite3


class DatabaseConnection:
    """
    Gerencia a conexão com o banco de dados SQLite.
    Define a abertura, o fechamento e a persistência (commit).
    """

    def __init__(self, db_name="escola.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """Abre a conexão com o banco de dados e configura o RowFactory."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()

            # Ativa o suporte a FOREIGN KEYs no SQLite, essencial para integridade
            self.cursor.execute("PRAGMA foreign_keys = ON;")

    def close(self):
        """Fecha a conexão com o banco de dados, salvando as alterações."""
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.cursor = None
