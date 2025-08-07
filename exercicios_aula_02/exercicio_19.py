saldo = 1000.00
while True:
    print("\n--- CAIXA ELETRÔNICO ---")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Ver saldo")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        saque = float(input("Valor do saque: "))
        if saque <= saldo:
            saldo -= saque
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    elif opcao == "2":
        deposito = float(input("Valor do depósito: "))
        saldo += deposito
        print("Depósito realizado com sucesso.")
    elif opcao == "3":
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    elif opcao == "4":
        print("Obrigado por usar nossos serviços.")
        break
    else:
        print("Opção inválida.")
