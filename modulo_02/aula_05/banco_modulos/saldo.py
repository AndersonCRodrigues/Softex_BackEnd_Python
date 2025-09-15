def verificar_saldo(usuario:dict) -> None:
    """Mostra para o usuario o saldo atual dele"""
    print(f"Seu saldo atual é de R$ {usuario["saldo"]:.2f}")
    print(f"Seu limite de cheque especial é de R$ {usuario["limite_cheque_especial"]:.2f}")

def sacar_valor(usuario:dict) -> None:
    """Permite ao usuario sacar um valor, verificando saldo"""
    try:
        valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
        if valor_a_sacar <= 0:
            print("Valor inválido.")
            return

        limite_total = usuario["saldo"] + usuario["limite_cheque_especial"]
        if valor_a_sacar <= limite_total:
            usuario["saldo"] -= valor_a_sacar
            print("Saque realizado com sucesso, retire seu valor.")
        else:
            print("Saldo insuficiente")
    except ValueError:
        print("Erro! Valor inválido, digite apenas números.")

def depositar_valor(usuario: dict) -> None:
    """Permite ao usuário depositar um valor na sua conta"""
    try:
        valor_depositar = float(input("Inisira o valor a ser depositado: "))
        if valor_depositar > 0:
            usuario["saldo"] += valor_depositar
            print("Depósito realizado com sucesso!")
            verificar_saldo(usuario)
        else:
            print("Valor inválido")
    except ValueError:
        print("Erro! Por favor, entre apenas no números.")