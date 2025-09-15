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
    
def alterar_senha(usuario: dict) -> None:
    """Permite ao usuáro alterar a senha, validando a senha antiga"""
    senha_antiga = input("Digite a sua senha antiga: ").strip()

    if senha_antiga != usuario["senha"]:
        print("Senha antiga incorreta!")
        return
    
    nova_senha1 = input("Digite a nova senha: ").strip()
    nova_senha2 = input("Repita a nova senha: ").strip()

    if nova_senha1 == nova_senha2:
        usuario["senha"] = nova_senha1
        print("Senha atualizada com sucesso!")
    else:
        print("As senhas não coincidem.")