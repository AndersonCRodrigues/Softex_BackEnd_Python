import sqlite3
from modulo_03.aula_06.database import DatabaseConnection


class StudentModel:
    """Gerencia a tabela 'alunos' (Um lado do N:N)."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de alunos."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """
        )
        self.db_conn.close()

    def create_student(self, nome, email):
        """Cria um novo aluno."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO alunos (nome, email) VALUES (?, ?);",
                (nome, email),
            )
            print(f"[SUCESSO] Aluno '{nome}' criado.")
        except sqlite3.IntegrityError:
            print(f"[ERRO] O e-mail '{email}' já está em uso.")
        finally:
            self.db_conn.close()

    def find_student_by_id(self, student_id):
        """Busca um aluno pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM alunos WHERE id = ?;", (student_id,))
        student = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return student

    def get_all_students(self):
        """Retorna todos os alunos."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM alunos;")
        students = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return students
