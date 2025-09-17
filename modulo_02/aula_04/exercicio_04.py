contatos: list[dict] = []


def adicionar_contato(nome: str, **informacoes: str) -> None:
    """Adiciona um novo contato à lista global."""
    novo_contato = {"nome": nome}
    novo_contato.update(informacoes)
    contatos.append(novo_contato)
    print(f"Contato '{nome}' adicionado com sucesso!")


def remover_contato(*nomes_a_remover: str) -> None:
    """Remove um ou mais contatos da lista por nome."""
    if not nomes_a_remover:
        print("Nenhum nome fornecido para remoção.")
        return

    removidos_count = 0
    for nome in nomes_a_remover:
        contato_encontrado = None
        for contato in contatos:
            if contato["nome"] == nome:
                contato_encontrado = contato
                break

        if contato_encontrado:
            contatos.remove(contato_encontrado)
            removidos_count += 1
            print(f"Contato '{nome}' removido.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    print(f"Total de contatos removidos: {removidos_count}")


def buscar_contato(nome_busca: str) -> dict | None:
    """Busca um contato por nome e retorna seu dicionário."""
    for contato in contatos:
        if contato["nome"] == nome_busca:
            return contato
    return None


def listar_contatos() -> None:
    """Lista todos os contatos salvos."""
    if contatos:
        print("\n--- Contatos Salvos ---")
        for i, contato in enumerate(contatos):
            print(
                f"{i+1}. Nome: {contato.get('nome')}, "
                f"Telefone: {contato.get('telefone', 'N/A')}, "
                f"Email: {contato.get('email', 'N/A')}"
            )
    else:
        print("Nenhum contato cadastrado.")


def menu_contatos():
    """Exibe o menu do gerenciador e coordena as operações."""
    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Procurar contato")
        print("4 - Listar todos")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone (opcional): ")
            email = input("Digite o e-mail (opcional): ")
            info = {}
            if telefone:
                info["telefone"] = telefone
            if email:
                info["email"] = email
            adicionar_contato(nome, **info)

        elif escolha == "2":
            nomes = input(
                "Digite o(s) nome(s) para remover (separado por vírgula): "
            ).split(",")
            nomes_limpos = [nome.strip() for nome in nomes]
            remover_contato(*nomes_limpos)

        elif escolha == "3":
            nome_busca = input("Digite o nome do contato: ")
            contato_encontrado = buscar_contato(nome_busca)
            if contato_encontrado:
                print(
                    f"Nome: {contato_encontrado['nome']} | "
                    f"Telefone: {contato_encontrado.get('telefone', 'N/A')} | "
                    f"E-mail: {contato_encontrado.get('email', 'N/A')}"
                )
            else:
                print("Contato não encontrado.")

        elif escolha == "4":
            listar_contatos()

        elif escolha == "5":
            print("Saindo do gerenciador.")
            break

        else:
            print("Opção inválida.")


menu_contatos()
