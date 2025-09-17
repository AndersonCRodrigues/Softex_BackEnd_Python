def carregar_dados_banco() -> dict:
    """Carrega os dados iniciais do banco, incluindo usuários e configurações."""
    return {
        "usuarios": {
            "123456-7": {
                "senha": "9999",
                "nome": "José",
                "saldo": 1500.00,
                "limite_cheque_especial": 500.00,
            }
        },
        "tentativas_login": 3,
        "ultima_conta_base": "123456",
        "digito_verificador": "7",
    }


def autenticar_usuario(
    dados_banco: dict, conta: str, senha: str
) -> tuple[bool, dict | None]:
    """Autentica o usuário com base na conta e senha. Retorna o status e o usuário."""
    usuario_encontrado = dados_banco["usuarios"].get(conta)
    if usuario_encontrado and usuario_encontrado["senha"] == senha:
        return True, usuario_encontrado
    return False, None


def cadastrar_cliente(dados_banco: dict) -> None:
    """Função para cadastrar um novo cliente no sistema."""
    print("\n--- Novo Cadastro de Cliente ---")

    ultima_conta_str: str = dados_banco["ultima_conta_base"]
    novo_numero_base: int = int(ultima_conta_str) + 1

    novo_numero_conta: str = f"{novo_numero_base}-{dados_banco['digito_verificador']}"

    if novo_numero_conta in dados_banco["usuarios"]:
        print("Erro: Esta conta já está cadastrada.")
        return

    nova_senha: str = input("Defina uma senha para o cliente: ")
    nome_cliente: str = input("Digite o nome do cliente: ")

    dados_banco["usuarios"][novo_numero_conta] = {
        "senha": nova_senha,
        "nome": nome_cliente,
        "saldo": 0.0,
        "limite_cheque_especial": 500.0,
    }

    dados_banco["ultima_conta_base"] = str(novo_numero_base)

    print(
        f"Cliente {nome_cliente} cadastrado com sucesso na conta {novo_numero_conta}."
    )


def listar_clientes(dados_banco: dict) -> None:
    """Lista todos os clientes cadastrados no sistema."""
    print("\n--- Clientes Cadastrados ---")
    if not dados_banco["usuarios"]:
        print("Nenhum cliente cadastrado ainda.")
        return

    for conta, usuario in dados_banco["usuarios"].items():
        print(f"Nome: {usuario['nome']} | Conta: {conta}")
    print("----------------------------")


def verificar_saldo(usuario: dict) -> None:
    """Mostra o saldo atual do usuário."""
    print(f"Seu saldo atual é de R$ {usuario['saldo']:.2f}.")
    print(
        f"Seu limite de cheque especial é de R$ {usuario['limite_cheque_especial']:.2f}."
    )


def sacar_valor(usuario: dict) -> None:
    """Permite ao usuário sacar um valor, verificando o saldo."""
    try:
        valor_a_sacar: float = float(input("Entre com o valor a ser sacado: "))
        if valor_a_sacar <= 0:
            print("Valor inválido para saque.")
            return

        limite_total: float = usuario["saldo"] + usuario["limite_cheque_especial"]
        if valor_a_sacar <= limite_total:
            usuario["saldo"] -= valor_a_sacar
            print("Saque realizado com sucesso, retire seu valor!")
            verificar_saldo(usuario)
        else:
            print("Saldo insuficiente!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


def depositar_valor(usuario: dict) -> None:
    """Permite ao usuário depositar um valor em sua conta."""
    try:
        depositar: float = float(input("Insira o valor a ser depositado: "))
        if depositar > 0:
            usuario["saldo"] += depositar
            print("Depósito realizado com sucesso!")
            verificar_saldo(usuario)
        else:
            print("Valor inválido!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


def pagar_boleto(usuario: dict) -> None:
    """Permite ao usuário pagar um boleto, verificando o saldo."""
    try:
        boleto: float = float(input("Entre com o valor do boleto: "))
        limite_total: float = usuario["saldo"] + usuario["limite_cheque_especial"]
        if boleto > 0 and boleto <= limite_total:
            usuario["saldo"] -= boleto
            print("Boleto pago com sucesso!")
            verificar_saldo(usuario)
        else:
            print("Saldo insuficiente ou valor inválido!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


def alterar_senha(usuario: dict) -> None:
    """Permite ao usuário alterar sua senha, validando a senha antiga."""
    senha_antiga: str = input("Digite a senha antiga: ")
    if senha_antiga != usuario["senha"]:
        print("Senha antiga incorreta!")
        return

    senha_nova1: str = input("Digite a nova senha: ")
    senha_nova2: str = input("Repita a nova senha: ")
    if senha_nova1 == senha_nova2:
        usuario["senha"] = senha_nova1
        print("Senha atualizada com sucesso!")
    else:
        print("As senhas não coincidem!")


def menu_operacoes(usuario: dict) -> None:
    """Exibe o menu de operações e executa a escolha do usuário."""
    while True:
        print(f"\nBem-vindo(a), {usuario['nome']}!")
        print("Escolha uma opção:")
        print("1- Ver saldo.")
        print("2- Sacar valor.")
        print("3- Depositar.")
        print("4- Pagar Boleto.")
        print("5- Alterar senha.")
        print("6- Sair.")

        opcao: str = input("Opção: ")

        if opcao == "1":
            verificar_saldo(usuario)
        elif opcao == "2":
            sacar_valor(usuario)
        elif opcao == "3":
            depositar_valor(usuario)
        elif opcao == "4":
            pagar_boleto(usuario)
        elif opcao == "5":
            alterar_senha(usuario)
        elif opcao == "6":
            print("Atendimento Finalizado")
            break
        else:
            print("Opção Inválida")


def iniciar_programa():
    """Inicia o loop principal do programa de banco."""
    dados_banco = carregar_dados_banco()

    while True:
        print("\n--- Terminal Bancário ---")
        print("1. Acessar Conta")
        print("2. Listar Clientes")
        print("3. Cadastrar Novo Cliente")
        print("4. Encerrar Atendimento")

        escolha_principal: str = input("Escolha uma opção: ")

        if escolha_principal == "1":
            acesso_permitido: bool = False
            for _ in range(dados_banco["tentativas_login"]):
                conta: str = input("Entre com a sua conta corrente: ")
                senha: str = input("Entre com a sua senha: ")
                acesso_permitido, usuario_atual = autenticar_usuario(
                    dados_banco, conta, senha
                )

                if acesso_permitido:
                    menu_operacoes(usuario_atual)
                    break
                else:
                    print("Conta ou senha inválida!")

            if not acesso_permitido:
                print("Número de tentativas excedido. Atendimento encerrado.")
        elif escolha_principal == "2":
            listar_clientes(dados_banco)
        elif escolha_principal == "3":
            cadastrar_cliente(dados_banco)
        elif escolha_principal == "4":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida.")


iniciar_programa()
