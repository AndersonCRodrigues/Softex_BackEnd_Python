usuarios: dict = {}


def validar_senha(senha: str) -> bool:
    """Valida se a senha atende aos critérios de segurança."""
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if "a" <= caractere <= "z":
            tem_minuscula = True
        elif "A" <= caractere <= "Z":
            tem_maiuscula = True
        elif "0" <= caractere <= "9":
            tem_numero = True

    if not tem_maiuscula or not tem_minuscula or not tem_numero:
        print("A senha deve conter maiúscula, minúscula e número.")
        return False

    return True


def registrar_usuario() -> None:
    """Permite ao usuário registrar um novo login."""
    usuario: str = input("Digite o nome de usuário: ")
    if usuario in usuarios:
        print("Usuário já existe.")
        return

    senha = input(
        "Digite a senha (mínimo 8 caracteres, com maiúscula, minúscula e número): "
    )
    if validar_senha(senha):
        usuarios[usuario] = senha
        print(f"Usuário '{usuario}' registrado com sucesso.")
    else:
        print("Falha no registro. Senha inválida.")


def autenticar_usuario() -> bool:
    """Verifica se as credenciais fornecidas correspondem a um usuário existente."""
    usuario: str = input("Usuário: ")
    senha: str = input("Senha: ")

    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False


def menu_login():
    """Exibe o menu do sistema de login e coordena as operações."""
    while True:
        print("\n=== SISTEMA DE LOGIN ===")
        print("1 - Cadastrar usuário")
        print("2 - Fazer login")
        print("3 - Sair")
        escolha: str = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_usuario()
        elif escolha == "2":
            if autenticar_usuario():
                print("Bem-vindo(a)!")
        elif escolha == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")


menu_login()
