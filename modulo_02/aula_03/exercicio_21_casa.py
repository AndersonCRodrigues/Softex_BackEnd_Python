contatos = {}

while True:
    opcao = input("Digite: 1(Adicionar Contato), 2(Buscar), 3(Sair) ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ").lower()
        numero = input("Digite o número do contato:")
        contatos[nome] = numero
    elif opcao == "2":
        nome = input("Digite o nome do contato: ").lower()
        contato = contatos.get(nome, "Contato não encontrado!")
        print(contato)
    elif opcao == "3":
        print("Encerrando Programa!")
        break
    else:
        print("Opção inválida")
