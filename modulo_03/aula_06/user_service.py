# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:

    def __init__(self):
        """
        crie um atributo que receberá a UserModel como composição
        """
        self.user_model = UserModel()

    def _safe_user_data(self, user: dict) -> dict | None:
        """
        este é um método privado que recebe um usuarios do banco.
        verifique se o usuários existe e então retorne ele sem a sua senha
        caso ele ão exista retorne None
        """
        if user:
            user.pop("senha_hash", None)
            return user
        return None

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str = "edit_self",
    ) -> bool:
        """
        Método que verifica o perfil do usuários, se for Diretoria retorne true
        Se não tiver target_user_id retorn false
        Se action == "edit_self" retorne current_user_id == target_user_id
        No geral retorn false
        """
        if current_user_profile == "Diretoria":
            return True
        if not target_user_id:
            return False
        if action == "edit_self":
            return current_user_id == target_user_id
        return False

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        """
        Método para criar um usuários.
        o campo senha deve ter no mínimo 8 caracteres, caso contrário retorne False a mensagem de erro.
        O campo email deve ter pelo menos 10 caracteres, uma @ e terminar com .com, retorne False se não tiver e a mensagem de erro.
        O campo Nome deve ter apenas letras e não deve estar vazio, retorne False se não tiver e a mensagem de erro.
        Caso os campos atendas as requisições, faça o hash da senha e salve use o método create_user da User Model
        """
        if (
            not email
            or len(email) < 10
            or "@" not in email
            or not email.endswith(".com")
        ):
            return False, "Erro: Email inválido!"

        if not nome_completo or not nome_completo.replace(" ", "").isalpha():
            return False, "Erro: Nome completo deve conter apenas letras."

        if not senha or len(senha) < 8:
            return False, "Erros: senha inválida."

        senha_hash = hash_senha(senha)
        return self.user_model.create_user(senha_hash, email, nome_completo, perfil)

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuários, deve receber um email e senha não vazios
        Use o método do find_user_by_email para buscar o usuario
        Se houver usuarios faça a comparação da senha passada com a senha hash do DB
        Use a função verificar_senha, se tiver ok, retorn o usuarios pelo método privado _safe_user_data
        e a mensagem Login bem-sucedido!.
        Caso contrario retorne None e a mensagem de erro
        """
        if not email or not senha:
            return None, "Erro: Email e senha não podem ser vazios."

        user = self.user_model.find_user_by_email(email)

        if user and verificar_senha(senha, user.get("senha_hash", "")):
            safe_user = self._safe_user_data(user)
            return safe_user, "Login bem-sucedido!"

        return None, "Erro: Email ou senha inválidos."

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        """
        Método para atualizar usuários.
        Chame o método privado _is_authorized, se o retorno for false, retorne false e acesso negado
        Confira as chaves em new_data (senha, nome_completo, email), se pelo menos um desses campos,
        Caso não haja nenhum valor a ser atualizado, encerre a função com False e mensagem de erro.
        Caso contrátio, chame o método da UserModel update_user_by_id passando o id e o new data
        """
        if not self._is_authorized(
            current_user_id, current_user_profile, target_user_id
        ):
            return False, "Acesso Negado!"

        update_data = {}

        if new_data.get("senha"):
            if len(new_data["senha"]) < 8:
                return False, "Erro: A nova senha deve ter no mínimo 8 caracteres."
            update_data["senha_hash"] = hash_senha(new_data["senha"])

        if new_data.get("email"):
            if (
                len(new_data["email"]) < 10
                or "@" not in new_data["email"]
                or not new_data["email"].endswith(".com")
            ):
                return False, "Erro: O novo email é inválido."
            update_data["email"] = new_data["email"]

        if new_data.get("nome_completo"):
            if not new_data["nome_completo"].replace(" ", "").isalpha():
                return False, "Erro: O novo nome deve conter apenas letras."
            update_data["nome_completo"] = new_data["nome_completo"]

        if update_data:
            return self.user_model.update_user_by_id(target_user_id, update_data)

        return False, "Nenhum dado válido para atualização fornecido."

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Método para deletar usuarios.
        So é permitido deletar usuarios se o current_user_profile for Diretoria.
        Caso não seja retorn false e a mensagem de acesso negado
        Senão chame o método delete_user_by_id, passando o id do usuários
        """
        if current_user_profile != "Diretoria":
            return False, "Acesso Negado: Somente a 'Diretoria' pode deletar usuários."

        return self.user_model.delete_user_by_id(user_id)

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Método para pegar um usuarios pelo id
        Retorne o usuarios apos passar pelo método _safe_user_data
        """
        user = self.user_model.find_user_by_id(user_id)
        if user:
            return self._safe_user_data(user)

        return None

    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        retorne todos os usuáriso apos passar pelo método _safe_user_data
        """
        users = self.user_model.get_all_users()
        safe_users = []
        for user in users:
            safe_user = self._safe_user_data(user)
            if safe_user:
                safe_users.append(safe_user)
        return safe_users
