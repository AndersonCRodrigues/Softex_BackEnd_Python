import saldo
# import banco_dados


def pagar_boleto(usuario: dict) -> None:
    """Permite ao usuário pagar um boleto, verificando saldo"""
    try:
        valor_boleto = float(input("Entre com o valor do boleto a ser pago: "))
        limite_total = usuario["saldo"] + usuario["limite_cheque_especial"]

        if valor_boleto > 0 and valor_boleto <= limite_total:
            usuario["saldo"] -= valor_boleto
            print("Boleto pago com sucesso!")
            saldo.verificar_saldo(usuario)

        else:
            print("Saldo insuficiente ou valor inválido!")
    
    except ValueError:
        print("Erro! Por favor, digite apenas números.")


# dados = banco_dados.banco_dados()
# usuario = dados["usuarios"]["123456-7"]

# pagar_boleto(usuario)