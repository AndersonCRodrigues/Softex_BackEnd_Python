# main.py
from user_service import UserService
from typing import Optional, Dict

# Simula a sessão do usuário logado
CURRENT_USER_SESSION: Dict[str, Optional[str] | Optional[int]] = {
    "id": None,
    "perfil": "Deslogado",
}


def display_menu():
    """Exibe o menu de opções."""
    print(
        f"\n--- Gerenciador de Usuários (Logado como: {CURRENT_USER_SESSION['perfil']}) ---"
    )
    options = [
        "1. Cadastrar novo usuário (Email, Nome, Senha)",
        "2. Fazer Login",
        "3. Buscar usuário por ID",
        "4. Editar *Meu* Perfil",
    ]
    for opt in options:
        print(opt)
    if CURRENT_USER_SESSION["perfil"] == "Diretoria":
        print("5. Deletar *Qualquer* Usuário (Diretoria)")
    else:
        print("5. (Acesso Restrito: Deletar Usuário)")
    remaining = [
        "6. Listar todos os usuários",
        "7. Logout",
        "8. Sair",
    ]
    for opt in remaining:
        print(opt)
    print("---------------------------------")


def main():
    """Função principal do programa."""
    user_service = UserService()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            print("\n--- Cadastro de Usuário ---")
            senha = input("Senha: ")
            email = input("E-mail: ")
            nome = input("Nome Completo: ")
            print(
                "Perfis: [Afiliado (Padrão), Associado, Diretoria, Coletivo/Institucional]"
            )
            perfil = input("Perfil de Acesso (Afiliado): ") or "Afiliado"

            success, message = user_service.register_user(senha, email, nome, perfil)
            print(message)
            input("\nPressione Enter para continuar...")

        elif choice == "2":
            print("\n--- Login de Usuário ---")
            email = input("E-mail: ")
            senha = input("Senha: ")

            user, message = user_service.login_user(email, senha)
            print(message)
            if user:
                CURRENT_USER_SESSION["id"] = user["id"]
                CURRENT_USER_SESSION["perfil"] = user["perfil_acesso"]
                print(f"Login bem-sucedido! Bem-vindo(a), {user['nome_completo']}.")
            input("\nPressione Enter para continuar...")

        elif choice == "3":
            print("\n--- Buscar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user = user_service.get_user_by_id(user_id)
                if user:
                    print(
                        f"\nUsuário encontrado: ID: {user['id']} | Perfil: {user['perfil_acesso']} | Nome: {user['nome_completo']}"
                    )
                    print(f"E-mail: {user['email']}")
                else:
                    print("Usuário não encontrado.")
            except ValueError:
                print("ID inválido.")
            input("\nPressione Enter para continuar...")

        elif choice == "4":
            print("\n--- Editar *Meu* Perfil ---")
            if not CURRENT_USER_SESSION["id"]:
                print("Você precisa estar logado para editar seu perfil.")
                input("\nPressione Enter para continuar...")
                continue

            print(f"Editando Perfil ID: {CURRENT_USER_SESSION['id']}")
            print("Deixe em branco os campos que não deseja alterar.")
            new_data = {
                "nome_completo": input("Novo Nome Completo: ") or None,
                "email": input("Novo E-mail: ") or None,
                "senha": input("Nova Senha: ") or None,
            }

            success, message = user_service.update_user_profile(
                CURRENT_USER_SESSION["id"],
                CURRENT_USER_SESSION["perfil"],
                CURRENT_USER_SESSION["id"],
                new_data,
            )
            print(message)
            input("\nPressione Enter para continuar...")

        elif choice == "5":
            print("\n--- Deletar Usuário ---")

            if CURRENT_USER_SESSION["perfil"] != "Diretoria":
                print("Acesso negado. Apenas a Diretoria pode deletar usuários.")
                input("\nPressione Enter para continuar...")
                continue

            try:
                user_id = int(input("Digite o ID do usuário a ser deletado: "))
                success, message = user_service.delete_user(
                    CURRENT_USER_SESSION["perfil"], user_id
                )
                print(message)
            except ValueError:
                print("ID inválido.")
            input("\nPressione Enter para continuar...")

        elif choice == "6":
            print("\n--- Lista de Usuários ---")
            users = user_service.get_all_users()
            if users:
                for user in users:
                    print(
                        f"ID: {user['id']} | Perfil: {user['perfil_acesso']} | Nome: {user['nome_completo']} | E-mail: {user['email']}"
                    )
            else:
                print("Nenhum usuário cadastrado.")
            input("\nPressione Enter para continuar...")

        elif choice == "7":
            print("Logout realizado.")
            CURRENT_USER_SESSION["id"] = None
            CURRENT_USER_SESSION["perfil"] = "Deslogado"
            input("\nPressione Enter para continuar...")

        elif choice == "8":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
