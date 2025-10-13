from user_model import UserModel


def display_menu():
    """Exibe o menu de opções."""
    print("\n--- Gerenciador de Usuários ---")
    print("1. Cadastrar novo usuário")
    print("2. Buscar usuário por ID")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Listar todos os usuários")
    print("6. Sair")
    print("---------------------------------")


def main():
    """Função principal do programa."""
    user_model = UserModel()

    while True:
        display_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            print("\n--- Cadastro de Usuário ---")
            senha = input("Senha: ")
            email = input("E-mail: ")
            user_model.create_user(senha, email)

        elif choice == "2":
            print("\n--- Buscar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user = user_model.find_user_by_id(user_id)
                if user:
                    print("\nUsuário encontrado:")
                    print(f"ID: {user['id']}")
                    print(f"E-mail: {user['email']}")
                    print(f"Data de Criação: {user['data_criacao']}")
                else:
                    print("Usuário não encontrado.")
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "3":
            print("\n--- Atualizar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                print("Deixe em branco os campos que não deseja alterar.")
                senha = input("Nova senha: ") or None
                email = input("Novo e-mail: ") or None
                user_model.update_user_by_id(user_id, senha, email)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "4":
            print("\n--- Deletar Usuário ---")
            try:
                user_id = int(input("Digite o ID do usuário: "))
                user_model.delete_user_by_id(user_id)
            except ValueError:
                print("ID inválido. Por favor, digite um número.")

        elif choice == "5":
            print("\n--- Lista de Usuários ---")
            users = user_model.get_all_users()
            if users:
                for user in users:
                    print(f"\nID: {user['id']}")
                    print(f"E-mail: {user['email']}")
                    print(f"Data de Criação: {user['data_criacao']}")
                print("\n--- Fim da lista ---")
            else:
                print("Nenhum usuário cadastrado.")

        elif choice == "6":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

