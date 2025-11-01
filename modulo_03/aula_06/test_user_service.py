import pytest
from user_service import UserService


@pytest.fixture(autouse=True)
def mock_hasher(mocker):
    mocker.patch("user_service.hash_senha", side_effect=lambda s: f"HASHED_{s}")
    mocker.patch(
        "user_service.verificar_senha", side_effect=lambda s, h: f"HASHED_{s}" == h
    )


@pytest.fixture
def user_service(mocker):

    mocker.patch("user_service.UserModel", autospec=True)
    return UserService()


DB_USER_DATA = {
    "id": 1,
    "email": "test@dominio.com",
    "nome_completo": "Nome Teste",
    "perfil_acesso": "Afiliado",
    "senha_hash": "HASHED_12345678",
    "data_criacao": "2023-01-01",
    "data_atualizacao": "2023-01-01",
}

SAFE_USER_DATA = {
    "id": 1,
    "email": "test@dominio.com",
    "nome_completo": "Nome Teste",
    "perfil_acesso": "Afiliado",
    "data_criacao": "2023-01-01",
    "data_atualizacao": "2023-01-01",
}


def test_safe_user_data_returns_safe_dict(user_service):
    safe_data = user_service._safe_user_data(DB_USER_DATA.copy())
    assert safe_data == SAFE_USER_DATA
    assert "senha_hash" not in safe_data


def test_safe_user_data_returns_none(user_service):
    assert user_service._safe_user_data(None) is None


@pytest.mark.parametrize(
    "current_id, current_profile, target_id, action, expected",
    [
        (1, "Diretoria", 10, "edit", True),
        (5, "Diretoria", 5, "delete", True),
        (1, "Afiliado", 1, "edit_self", True),
        (1, "Afiliado", 10, "edit_self", False),
        (1, "Afiliado", 10, "delete", False),
        (None, "Afiliado", 1, "edit_self", False),
        (1, "Afiliado", 0, "edit_self", False),
    ],
)
def test_is_authorized(
    user_service, current_id, current_profile, target_id, action, expected
):
    result = user_service._is_authorized(
        current_id,
        current_profile,
        target_id,
        action,
    )
    assert result == expected


@pytest.mark.parametrize(
    "senha, email, nome_completo, error_msg",
    [
        (
            "1234567",
            "valido@email.com",
            "Nome Valido",
            "Erros: senha inválida.",
        ),
        (
            "12345678",
            "inv.com",
            "Nome Valido",
            "Erro: Email inválido!",
        ),
        (
            "12345678",
            "valido@email.com",
            "123 Invalido",
            "Erro: Nome completo deve conter apenas letras.",
        ),
    ],
)
def test_register_user_validation_failures(
    user_service, senha, email, nome_completo, error_msg
):
    success, message = user_service.register_user(senha, email, nome_completo)
    assert success is False
    assert message == error_msg
    user_service.user_model.create_user.assert_not_called()


def test_register_user_success(user_service):
    user_service.user_model.create_user.return_value = (
        True,
        "Usuário criado com sucesso!",
    )

    senha = "senha_valida"
    email = "novo@usuario.com"
    nome = "Usuario Novo"
    perfil = "Gerente"

    success, message = user_service.register_user(senha, email, nome, perfil)

    assert success is True
    assert message == "Usuário criado com sucesso!"
    user_service.user_model.create_user.assert_called_once_with(
        "HASHED_senha_valida", email, nome, perfil
    )


def test_login_user_success(user_service):
    user_service.user_model.find_user_by_email.return_value = DB_USER_DATA
    user_data, message = user_service.login_user("test@dominio.com", "12345678")

    assert user_data == SAFE_USER_DATA
    assert message == "Login bem-sucedido!"
    user_service.user_model.find_user_by_email.assert_called_once_with(
        "test@dominio.com"
    )


def test_login_user_wrong_password(user_service):
    # Configura o retorno do mock do UserModel
    user_service.user_model.find_user_by_email.return_value = DB_USER_DATA

    user_data, message = user_service.login_user(
        "test@dominio.com", "senha_errada"
    )  # Senha que não resultará no hash correto

    assert user_data is None
    assert message == "Erro: Email ou senha inválidos."


def test_update_user_profile_success_all_fields(user_service):
    user_service.user_model.update_user_by_id.return_value = (
        True,
        "Usuário atualizado com sucesso!",
    )
    new_data = {
        "senha": "nova_senha_valida",
        "email": "novo@email.com",
        "nome_completo": "Novo Nome",
    }

    success, message = user_service.update_user_profile(
        current_user_id=1,
        current_user_profile="Afiliado",
        target_user_id=1,
        new_data=new_data,
    )

    assert success is True
    assert message == "Usuário atualizado com sucesso!"
    user_service.user_model.update_user_by_id.assert_called_once()

    target_id, update_dict = user_service.user_model.update_user_by_id.call_args[0]

    assert target_id == 1
    assert update_dict["senha_hash"] == "HASHED_nova_senha_valida"
    assert update_dict["email"] == "novo@email.com"
    assert update_dict["nome_completo"] == "Novo Nome"


def test_update_user_profile_validation_failure_email(user_service):
    new_data = {"email": "email_curto"}
    success, message = user_service.update_user_profile(
        current_user_id=1,
        current_user_profile="Afiliado",
        target_user_id=1,
        new_data=new_data,
    )
    assert success is False
    assert message == "Erro: O novo email é inválido."
    user_service.user_model.update_user_by_id.assert_not_called()


def test_delete_user_unauthorized(user_service):
    success, message = user_service.delete_user(
        current_user_profile="Afiliado", user_id=1
    )
    assert success is False
    assert message == "Acesso Negado: Somente a 'Diretoria' pode deletar usuários."
    user_service.user_model.delete_user_by_id.assert_not_called()


def test_delete_user_success(user_service):
    user_service.user_model.delete_user_by_id.return_value = (
        True,
        "Usuário deletado com sucesso!",
    )

    success, message = user_service.delete_user(
        current_user_profile="Diretoria", user_id=5
    )
    assert success is True
    assert message == "Usuário deletado com sucesso!"
    user_service.user_model.delete_user_by_id.assert_called_once_with(5)


def test_get_user_by_id_success(user_service):
    user_service.user_model.find_user_by_id.return_value = DB_USER_DATA

    user_data = user_service.get_user_by_id(1)

    assert user_data == SAFE_USER_DATA
    assert "senha_hash" not in user_data
    user_service.user_model.find_user_by_id.assert_called_once_with(1)


def test_get_all_users_success(user_service):
    user2_data = {
        "id": 2,
        "email": "user2@dominio.com",
        "nome_completo": "User Dois",
        "perfil_acesso": "Diretoria",
        "senha_hash": "HASHED_senha2",
        "data_criacao": "2023-01-02",
        "data_atualizacao": "2023-01-02",
    }
    safe_user2_data = {
        "id": 2,
        "email": "user2@dominio.com",
        "nome_completo": "User Dois",
        "perfil_acesso": "Diretoria",
        "data_criacao": "2023-01-02",
        "data_atualizacao": "2023-01-02",
    }

    user_service.user_model.get_all_users.return_value = [
        DB_USER_DATA.copy(),
        user2_data.copy(),
    ]

    all_users = user_service.get_all_users()

    assert all_users == [SAFE_USER_DATA, safe_user2_data]
    user_service.user_model.get_all_users.assert_called_once()
