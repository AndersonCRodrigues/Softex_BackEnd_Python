opcao = ""

while opcao != "4":
    print("\nMenu:")
    print("1 - Texto para maiúsculas")
    print("2 - Texto para minúsculas")
    print("3 - Contar letra")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        texto = input("Digite o texto: ")
        print(texto.upper())
    elif opcao == "2":
        texto = input("Digite o texto: ")
        print(texto.lower())
    elif opcao == "3":
        texto = input("Digite o texto: ").lower()
        letra = input("Digite a letra: ").lower()
        cont = 0
        i = 0
        while i < len(texto):
            if texto[i] == letra:
                cont += 1
            i += 1
        print("A letra aparece", cont, "vezes")
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida!")
