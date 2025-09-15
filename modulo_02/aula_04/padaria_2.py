"""
Comercio Padaria
x 1-O programa tem que rodar em loop infinito até ser parado
x 2-cliente pedir um tipo de pão (frances, doce, forma, australiano)
x 3-cada pao terá uma quantidade
x 4-valor do pao
x 5-pedir forma de pagameno (dinheiro, cartao)
x 6-forma de entrega
x 7-dados do cliente (se for entregar)
x 8-valor do frete por bairro
x 9-nome do atendente
x 10-codigo da entrega
"""
def dados() -> dict:
    """Carregar e retornar os dado de produtos, frete e funcionários"""
    return {
        "atendente": "Maria",
        "paes": {
            "frances": {"nome": "Pão Francês", "valor": 0.50, "quantidade": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "quantidade": 20},
            "forma": {"nome": "Pão de Forma", "valor": 5.99, "quantidade": 18},
        },
        "bairros": {
            "barroco": {"nome": "Barroco", "frete": 5.00},
            "sao jose": {"nome": "São José", "frete": 15.00},
        },
        "codigo_venda_base": 95875,
    }

def obter_dados_cliente() -> dict:
    """Solicitar e retornar os dados do cliente"""
    nome = input("Informe seu nome: ")
    return {"nome": nome}

def solicitar_forma_pagamento() -> str:
    """Solicitar e retornar a forma de pagamento escolhida"""
    while True:
        pagamento = input("Escolha a forma de pagamento (1-Dinheiro, 2-Cartão)")
        if pagamento == "1":
            return "Dinheiro"
        elif pagamento == "2":
            return "Cartão"
        else:
            print("Forma de pagamento inválida")

def gerar_codigo_venda(codigo_base: int) -> int:
    """Gera e retorna o código de venda"""
    return codigo_base + 1

def calcula_frete(bairros_disponives: dict) -> tuple[str, float]:
    """Calcula o valor do frete com base no bairro de entrega"""
    print("Bairros para entrega")
    while True:
        for bairro in bairros_disponives.values():
            print(f"- {bairro["nome"]}" )
        
        bairro_entrega_nome = input("Qual o bairro de entrega?").lower()

        bairro_encontrado = ""

        for chave, bairro in bairros_disponives.values():
            if bairro["nome"].lower() == bairro_entrega_nome:
                bairro_encontrado = chave
                break
        
        if not bairro_encontrado:
            print("Bairro fora da área de entrega")
        else:
            frete = bairros_disponives[bairro_encontrado]["frete"]
            return bairro_entrega_nome, frete
        
def cadastrar_produto(estoque: dict) -> None:
    """Permite ao atendente cadastrar um novo produto"""
    nome_produto = input("Digite o nome do novo produto (identificador)").lower().strip()

    if nome_produto in estoque:
        print("Erro! Produto já cadastrado com este identificador!!!")
        return

    try:
        nome_completo = input("Digite o nome completo do produto: ").strip()
        valor = float(input("Digite o valor do novo produto: "))
        quantidade = int(input("Digite a quantidade inicial do produto: "))

        if nome_produto and nome_completo and valor > 0 and quantidade > 0:
            estoque[nome_produto] = {"nome": nome_completo, "valor": valor, "quantidade": quantidade}
            print(f"Produto {nome_completo} cadastrado com sucesso!")
        
        else:
            print("Erro! Dados inválidos.")
    
    except ValueError:
        print("Entrada de dados inválida.")

def atualizar_produto(estoque: dict) -> None:
    """Permite ao atendete atualizar um produto existente"""
    nome_produto = input("Digite o nome do produto para atualizar (identificador): ").lower()

    if nome_produto not in estoque:
        print("Produto não cadastrado")
        return
    
    print(f"Produto '{estoque[nome_produto]}' selecionado.")
    escolha = input("O que deseja atualizar?\n \
          1 - Valor\n \
          2 - Quantidade")
    
    try:
        if escolha == "1":
            novo_valor = float(input("Digite o novo valor do produto: "))
            if novo_valor > 0:
                estoque[nome_produto]["valor"] = novo_valor
                print(f"Valor atualizado para R$ {novo_valor:.2f} ")
            else:
                print("Valor inválido.")
        elif escolha == "2":
            nova_quantidade = int(input("Digite a nova quantidade do produto "))
            if nova_quantidade > 0:
                 estoque[nome_produto]["quantidade"] += nova_quantidade
                 print(f"Quantidade atual de {estoque[nome_produto]["quantidade"]} itens.")
            else:
                print("Quantidade inválida! ")
        else:
            print("Erro! Opção inválida.")
    except ValueError:
        print("Erro! Entrada de dados inválida. Digite apenas números.")

def cadastrar_localidade(bairros: dict) -> None:
    """Permite ao atendente cadastrar um novo bairro para entrega"""
    nome_bairro = input("Digite o nome do bairro (identificarod)").lower().strip()
    
    if nome_bairro in bairros:
        print("Erro! Bairro já cadastrado.")
        return
    
    try:
        nome_completo = input("Digite o nome completo do bairro: ").strip()
        valor_frete = float(input(f"Digite o valor do frete para o bairro {nome_completo}: "))

        if nome_bairro and valor_frete >= 0 and nome_completo:
            bairros[nome_bairro]= {"nome": nome_completo, "frete": valor_frete}
            print(f"Localidade {nome_completo} com frete de R$ {valor_frete:.2f} cadastrado com sucesso!")
        else:
            print("Dados inválidos! O cadastro não foi realizado.")

    except ValueError:
        print("Entrada inválida! O valor do frete deve ser um número.")

def processar_pedido(paes_disponiveis: dict) -> tuple[dict, int, float, dict] | None:
    """
    Processa o pedido do cliente, verifica o estoque e calcula o frete.
    Retorna uma tupla com o dicionario do pão, quantidade,
    valor total da compra e o dicionario atualizado de pães.
    """
    print("Temos os seguintes pães:")
    for pao in paes_disponiveis.values():
        print(f" - {pao["nome"]}")

    escolha_pao = input("Qual pão você deseja?: ").lower().strip()
    pao_encontrado = ""

    for chave, pao in paes_disponiveis.items():
        if pao["nome"].lower() == escolha_pao:
            pao_encontrado = chave
            break

    if not pao_encontrado:
        print("Opção inválida!")
        return None
    
    pao_escolhido = paes_disponiveis[pao_encontrado]

    try:
        quantidade = int(input(f"Digite a quantidade do {pao_escolhido["nome"]}: "))

        if quantidade <= 0:
            print("Quantidade inválida!")
            return None
    except ValueError:
        print("Erro! Quantidade deve ser um número inteiro.")
        return None
    
    if quantidade > pao_escolhido["quantidade"]:
        print(f"Infelizmente só tenho {pao_escolhido["quantidade"]} unidades deste pão.")
        return None

    paes_disponiveis[pao_encontrado]["quatidade"] -= quantidade
    valor_compra = quantidade * pao_escolhido["valor"]

    return pao_escolhido, quantidade, valor_compra, paes_disponiveis

def iniciar_programa() -> None:
    """Função que inicia o loop principal do programa de vendas"""
    banco_dados = dados()
    atendente = banco_dados["atendente"]
    paes_estoque = banco_dados["paes"]
    bairros_disponiveis = banco_dados["bairros"]
    codigo_venda = banco_dados["codigo_venda_base"]

    while True:
        print(f"-- Bem vindo(a) a Padaria Desespero, sou o(a) atendente {atendente}.")
        print("-- Menu Principal --")
        print("1. Iniciar vendas")
        print("2. Gerenciar Produtos")
        print("3. Cadastrar Nova Localidade")
        print("4. Sair do Sistema")

        opcao = input("Escolha a sua opção: ")

        if opcao == "1":
            pedido = processar_pedido(paes_estoque)

            if not pedido:
                continue

            pao_escolhido, qtd_pedido, valor_compra, paes_estoque = pedido

            print(f"Seu pedido foi de {qtd_pedido} {pao_escolhido['nome']} ficou em R$ {valor_compra:.2f}.")

            forma_retirada = input("É para 1. retirar ou 2.entregar? ")
            valor_frete = 0.0

            if forma_retirada == "2":
                bairro, valor_frete = calcula_frete(bairros_disponiveis)
                print(f"Valor do frete para o bairro {bairros_disponiveis[bairro]["nome"]} é de R$ {valor_frete:.2f}")


            dados_cliente = obter_dados_cliente()
            forma_pagamento = solicitar_forma_pagamento()

            valor_total_compra = valor_frete + valor_compra
            cod_venda = gerar_codigo_venda(codigo_venda)
            banco_dados["codigo_venda_base"] = cod_venda

            print("-- Resumo da veda --")
            print(f"Cliente: {dados_cliente["nome"]}")
            print(f"Valor dos pães: R$ {valor_compra:.2f}")
            print(f"Valor do frete: R$ {valor_frete:2f}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Valor total da compra R$ {valor_total_compra}")
            print(f"Código da entrega: {cod_venda}")
        elif opcao == "2":
            pass
        elif opcao == "3":
            pass
        elif opcao == "4":
            print("Saindo do sistema. Até a próxima.")
            break
        else:
            print("Opção inválida.")
