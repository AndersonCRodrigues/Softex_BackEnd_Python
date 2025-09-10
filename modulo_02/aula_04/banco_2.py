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

def banco() -> dict:
    """Carrega os dados inicias do banco dados, que inclui usuario e configurações"""
    return {
        "usuarios": {
            "123456-7": {
                "senha": "9999",
                "nome": "José",
                "saldo": 1500.00,
                "limite_cheque_especial": 500.00,
            },
        },
        "tentavas_login": 3,
        "ultima_conta_base": "123456",
        "digito_verificador": "7",
    }

def autenticar_usuario(
        dados_banco:dict, 
        conta:str,
        senha:str,
        ) -> tuple[bool, dict | None]:
    """Autentica o usuario com base na conta e senha. Retorna o status e o usuario"""
    usuario_encontrado = dados_banco["usuarios"].get(conta, None) # None == nada

    if usuario_encontrado and usuario_encontrado["senha"] == senha:
        return True, usuario_encontrado
    
    return False, None

def verificar_saldo(usuario:dict) -> None:
    """Mostra para o usuario o saldo atual dele"""
    print(f"Seu saldo atual é de R$ {usuario["saldo"]:.2f}")
    print(f"Seu limite de cheque especial é de R$ {usuario["limite_cheque_especial"]:.2f}")

def cadastrar_cliente(dados_banco:dict) -> None:
    """Cadastra um novo usuário no sistema"""
    print("--- Novo cadastro de Cliente ---")

    ultima_conta = dados_banco["ultima_conta_base"]
    nova_conta = int(ultima_conta) + 1

    novo_numero_conta = f"{nova_conta}-{dados_banco["digito_verificador"]}"

    if novo_numero_conta in dados_banco["usuarios"]:
        print("Erro! Está conta já esta cadastrada.")
        return
    
    nova_senha = input("Defina uma senha para sua conta: ")
    nome_cliente = input("Defina o nome do cliente: ")

    dados_banco["usuarios"][novo_numero_conta] = {
        "senha": nova_senha,
        "nome": nome_cliente,
        "saldo": 0.00,
        "limite_cheque_especial": 500.00
    }

    dados_banco["ultima_conta_base"] = str(nova_conta)
    print(f"Cliente {nome_cliente} cadastrado com sucesso na conta {novo_numero_conta}.")

def listar_clientes(banco_dados:dict) -> None:
    """Lista todos os clientes cadastrados no sistema"""
    print("\n--- Clientes Cadastrados ---")

    if not banco_dados["usuarios"]:
        print("Nenhum cliente cadastrado")
        return
    
    for conta, usuario in banco_dados["usuarios"].items():
        print(f"Nome: {usuario["nome"]} | Conta: {conta}")
        print("-"*30)

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