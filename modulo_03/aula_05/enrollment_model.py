from modulo_03.aula_06.database import DatabaseConnection
import sqlite3


class EnrollmentModel:
    """Gerencia a tabela 'matriculas', a junção para o relacionamento N:N."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de matrícula com chaves estrangeiras e a chave primária composta."""
        self.db_conn.connect()

        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS matriculas (
                id_aluno INTEGER NOT NULL,
                id_curso INTEGER NOT NULL,
                data_matricula DATETIME DEFAULT CURRENT_TIMESTAMP,

                -- Chave primária composta (evita matrícula duplicada)
                PRIMARY KEY (id_aluno, id_curso),

                -- FOREIGN KEYs para integridade
                FOREIGN KEY (id_aluno) REFERENCES alunos(id) ON DELETE CASCADE,
                FOREIGN KEY (id_curso) REFERENCES cursos(id) ON DELETE CASCADE
            );
        """
        )
        self.db_conn.close()

    def enroll_student(self, id_aluno, id_curso):
        """Matricula um aluno em um curso (Insert na tabela N:N)."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO matriculas (id_aluno, id_curso) VALUES (?, ?);",
                (id_aluno, id_curso),
            )
            print(
                f"[SUCESSO] Matrícula de aluno {id_aluno} no curso {id_curso} registrada."
            )
        except sqlite3.IntegrityError:
            print(
                "[ERRO] Falha na matrícula. Verifique se o aluno/curso existe ou se a matrícula já foi feita."
            )
        finally:
            self.db_conn.close()

    def get_courses_by_student(self, id_aluno):
        """Busca todos os cursos em que um aluno está matriculado.
        (Consulta N:N - Aluno -> Cursos)
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            SELECT c.id, c.nome, m.data_matricula
            FROM cursos c
            INNER JOIN matriculas m ON c.id = m.id_curso
            WHERE m.id_aluno = ?;
            """,
            (id_aluno,),
        )
        courses = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return courses

    def get_students_by_course(self, id_curso):
        """Busca todos os alunos matriculados em um curso específico.
        (Consulta N:N - Curso -> Alunos)
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            SELECT a.id, a.nome, a.email, m.data_matricula
            FROM alunos a
            INNER JOIN matriculas m ON a.id = m.id_aluno
            WHERE m.id_curso = ?;
            """,
            (id_curso,),
        )
        students = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return students
