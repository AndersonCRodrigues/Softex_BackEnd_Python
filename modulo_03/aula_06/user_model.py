# user_model.py
import sqlite3
from datetime import datetime
from database import DatabaseConnection


class UserModel:

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_table()

    def _create_table(self):
        """Cria a tabela de usuários simplificada (apenas login, nome e perfil)."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                senha_hash TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                nome_completo TEXT,
                perfil_acesso TEXT DEFAULT 'Afiliado',
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """
        )
        self.db_conn.close()

    def create_user(
        self,
        senha_hash: str,
        email: str,
        nome_completo: str,
        perfil_acesso: str,
    ) -> tuple[bool, str]:
        """Cria um novo usuário, usando colunas e placeholders explícitos."""
        self.db_conn.connect()

        field_names = "email, senha_hash, nome_completo, perfil_acesso"
        placeholders = "?, ?, ?, ?"

        params = (
            email,
            senha_hash,
            nome_completo,
            perfil_acesso,
        )

        try:
            self.db_conn.cursor.execute(
                f"""
                INSERT INTO usuarios ({field_names})
                VALUES ({placeholders});
            """,
                params,
            )
            self.db_conn.close()
            return True, "Usuário criado com sucesso!"
        except sqlite3.IntegrityError as e:
            self.db_conn.close()
            if "email" in str(e):
                return False, f"Erro: O e-mail '{email}' já está em uso."
            return False, f"Erro de integridade ao criar usuário: {e}"
        except Exception as e:
            self.db_conn.close()
            return False, f"Erro desconhecido: {e}"

    def find_user_by_id(self, user_id: int):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE id = ?;", (user_id,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user

    def find_user_by_email(self, email: str):
        """Busca um usuário pelo e-mail (usado no login)."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios WHERE email = ?;", (email,))
        user = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return user

    def update_user_by_id(
        self,
        user_id: int,
        updates_data: dict,
    ) -> tuple[bool, str]:
        """
        Atualiza informações de um usuário (email, nome_completo, senha_hash) de forma simples.
        A query é construída dinamicamente no SET para garantir flexibilidade de quais campos atualizar.
        """
        self.db_conn.connect()
        updates = []
        params = []

        if updates_data.get("senha_hash"):
            updates.append("senha_hash = ?")
            params.append(updates_data["senha_hash"])
        if updates_data.get("email"):
            updates.append("email = ?")
            params.append(updates_data["email"])
        if updates_data.get("nome_completo"):
            updates.append("nome_completo = ?")
            params.append(updates_data["nome_completo"])

        if not updates:
            self.db_conn.close()
            return False, "Nenhum dado válido para atualizar."

        # Adiciona data_atualizacao
        updates.append("data_atualizacao = ?")
        params.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        params.append(user_id)

        query_updates_str = ", ".join(updates)
        query = f"UPDATE usuarios SET {query_updates_str} WHERE id = ?;"

        try:
            self.db_conn.cursor.execute(query, params)
            rows_affected = self.db_conn.cursor.rowcount
            self.db_conn.close()
            if rows_affected > 0:
                return True, "Usuário atualizado com sucesso!"
            return False, "Usuário não encontrado."
        except sqlite3.IntegrityError:
            self.db_conn.close()
            return False, f"Erro: O e-mail já está em uso por outro usuário."
        except Exception as e:
            self.db_conn.close()
            return False, f"Erro desconhecido: {e}"

    def delete_user_by_id(self, user_id: int) -> Tuple[bool, str]:
        """Deleta um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (user_id,))
        rows_affected = self.db_conn.cursor.rowcount
        self.db_conn.close()
        if rows_affected > 0:
            return True, "Usuário deletado com sucesso!"
        return False, "Usuário não encontrado."

    def get_all_users(self):
        """Retorna todos os usuários."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM usuarios;")
        users = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return users
