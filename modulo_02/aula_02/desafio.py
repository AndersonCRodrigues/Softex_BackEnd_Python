registros_acessos = []
usuarios_sucesso = set()
tempo_total_sucesso = 0

print("--- Registro de Acessos ---")

while True:
    try:
        nome_usuario = input("\nDigite o nome de usuário (ou 'parar' para sair): ")
        if nome_usuario.lower() == "parar":
            break

        duracao_sessao = int(input("Digite a duração da sessão em minutos: "))

        print("Selecione o status:")
        print("1 - Sucesso")
        print("2 - Falha")
        opcao_status = input("Opção: ")

        if opcao_status == "1":
            status = "sucesso"
            usuarios_sucesso.add(nome_usuario)
            tempo_total_sucesso += duracao_sessao
        elif opcao_status == "2":
            status = "falha"
        else:
            print("Opção de status inválida. O registro não será salvo.")
            continue

        registros_acessos.append((nome_usuario, status, duracao_sessao))

    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a duração.")

print("\n" + "=" * 20)
print("RELATÓRIO DE ACESSOS")
print("=" * 20)

print("\nRegistros de acessos:")
print(registros_acessos)

print("\nUsuários com acesso bem-sucedido:")
print(usuarios_sucesso)

print("\nTempo total das sessões bem-sucedidas:")
print(f"{tempo_total_sucesso} minutos")
