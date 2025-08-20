"""
programa de banco
x 1- rodar em loop infinito
x 2- ter conta e senha (validar)
3- encerrar atendimento
4- cheque especial (limite saldo negativo)
x 5- tentar 3 vezes a senha
6- opções (saque, deposito, saldo)
7- mostrar saldo apos saque
8- alterar senha
x 9- dizer o nome do usuario
10- pagar boleto
"""

# declaração constantes
conta_corrente = "123456-7"
senha_usuario = "9999"
saldo_atual = 0
limite_saldo_negativo = 500.00
nome_usuario = "José"

while True:
    for i in range(3):
        conta = input("Entre com a sua conta corrente: ")
        senha = input("Entre com a sua senha: ")
        if conta == conta_corrente and senha == senha_usuario:
            print(f"Bem vindo {nome_usuario}!")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha inválida!")
            acesso_permitido = False

    if not acesso_permitido:
        break

    while True:
        opcao = input("Escolha uma opção:\n" \
        "1- Ver saldo.\n" \
        "2- Sacar valor.\n" \
        "3- Depositar.\n" \
        "4- Pagar Boleto.\n" \
        "5- Alterar senha.\n" \
        "6- Sair.\n")

        if opcao == "1":
            print(f"Seu saldo atual é de {saldo_atual}.")
        elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
                saldo -= valor_a_sacar
                print("Saldo liberado, retire seu valor!")
            else:
                print("Saldo insuficiente!")
        elif opcao == "3":
            depositar = float(input("Insira o valor a ser depositado: "))
            if depositar > 0:
                saldo += depositar
            else:
                print("Valor inválido!")
        elif opcao == "4":
            pass
        elif opcao == "5":
            pass
        elif opcao == "6":
            print("Atendimento Finanilzado")
            break
        else:
            print("Opção Inválida")