import sqlite3
from modulo_03.aula_06.database import DatabaseConnection


class CourseModel:
    """Gerencia a tabela 'cursos' (Outro lado do N:N)."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de cursos."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                descricao TEXT
            );
        """
        )
        self.db_conn.close()

    def create_course(self, nome, descricao):
        """Cria um novo curso."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO cursos (nome, descricao) VALUES (?, ?);",
                (nome, descricao),
            )
            print(f"[SUCESSO] Curso '{nome}' criado.")
        except sqlite3.IntegrityError:
            print(f"[ERRO] O curso '{nome}' já existe.")
        finally:
            self.db_conn.close()

    def find_course_by_id(self, course_id):
        """Busca um curso pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM cursos WHERE id = ?;", (course_id,))
        course = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return course

    def get_all_courses(self):
        """Retorna todos os cursos."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM cursos;")
        courses = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return courses
