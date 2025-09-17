def carregar_dados_padaria() -> dict:
    """Carrega e retorna todos os dados de produtos, frete e funcionários."""
    return {
        "atendente": "Maria",
        "paes": {
            "frances": {"nome": "Pão Francês", "valor": 0.50, "estoque": 15},
            "doce": {"nome": "Pão Doce", "valor": 5.00, "estoque": 20},
            "forma": {"nome": "Pão de Forma", "valor": 5.99, "estoque": 18},
        },
        "bairros": {
            "barroco": {"nome": "Barroco", "frete": 5.00},
            "sao jose": {"nome": "São José", "frete": 15.00},
        },
        "codigo_venda_base": 98568,
    }


def processar_pedido(
    paes_disponiveis: dict,
) -> tuple[dict, int, float, dict] | None:
    """
    Processa o pedido do cliente, verifica estoque e calcula o valor.
    Retorna uma tupla com o dicionário do pão, quantidade,
    valor total e o dicionário atualizado de pães.
    """
    print("Temos os pães:")
    for pao in paes_disponiveis.values():
        print(f"- {pao['nome']}")

    escolha_nome = input("Qual pão você deseja? ").lower()

    pao_encontrado_key = None
    for key, pao in paes_disponiveis.items():
        if pao["nome"].lower() == escolha_nome:
            pao_encontrado_key = key
            break

    if pao_encontrado_key is None:
        print("Opção de pão inválida.")
        return None

    pao_escolhido = paes_disponiveis[pao_encontrado_key]

    try:
        quantidade = int(input(f"Qual a quantidade de {pao_escolhido['nome']}? "))
        if quantidade <= 0:
            print("Quantidade inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return None

    if quantidade > pao_escolhido["estoque"]:
        print(f"Infelizmente só tenho {pao_escolhido['estoque']} pães no momento!")
        return None

    paes_disponiveis[pao_encontrado_key]["estoque"] -= quantidade

    valor_compra = quantidade * pao_escolhido["valor"]
    return pao_escolhido, quantidade, valor_compra, paes_disponiveis


def calcular_frete(bairros_disponiveis: dict) -> tuple[str, float] | None:
    """Calcula o valor do frete com base no bairro de entrega."""
    print("Bairros para entrega:")
    for bairro in bairros_disponiveis.values():
        print(f"- {bairro['nome']}")

    bairro_entrega_nome = input("Qual o bairro? ").lower()

    bairro_encontrado_key = None
    for key, bairro in bairros_disponiveis.items():
        if bairro["nome"].lower() == bairro_entrega_nome:
            bairro_encontrado_key = key
            break

    if bairro_encontrado_key is None:
        print("Bairro fora da área de entrega.")
        return None

    frete = bairros_disponiveis[bairro_encontrado_key]["frete"]
    return bairro_encontrado_key, frete


def obter_dados_cliente() -> dict:
    """Solicita e retorna os dados do cliente."""
    nome = input("Informe seu nome: ")
    return {"nome": nome}


def selecionar_forma_pagamento() -> str:
    """Permite ao cliente escolher a forma de pagamento."""
    pagamento = input("Escolha a forma de pagamento (1-dinheiro, 2-cartão): ")
    return "Dinheiro" if pagamento == "1" else "Cartão"


def gerar_codigo_venda(codigo_base: int) -> int:
    """Gera e retorna o código de venda."""
    return codigo_base + 1


def cadastrar_produto(estoque: dict) -> None:
    """Permite ao atendente cadastrar um novo tipo de pão."""
    nome_pao = input("Digite o nome do novo pão (identificador): ").lower()
    if nome_pao in estoque:
        print(
            f"Erro: O pão '{nome_pao}' já está cadastrado. Use a opção de atualização."
        )
        return

    try:
        nome_completo = input("Digite o nome completo do pão: ")
        valor = float(input("Digite o valor do pão: "))
        qtd_estoque = int(input("Digite a quantidade inicial em estoque: "))
        if nome_pao and valor > 0 and qtd_estoque >= 0:
            estoque[nome_pao] = {
                "nome": nome_completo,
                "valor": valor,
                "estoque": qtd_estoque,
            }
            print(f"Pão '{nome_completo}' cadastrado com sucesso!")
        else:
            print("Dados inválidos. O cadastro não foi realizado.")
    except ValueError:
        print("Entrada inválida. O valor e a quantidade devem ser números.")


def atualizar_produto(estoque: dict) -> None:
    """Permite ao atendente atualizar um produto existente."""
    nome_pao = input("Digite o nome do pão que deseja atualizar: ").lower()
    if nome_pao not in estoque:
        print("Erro: O pão não está cadastrado.")
        return

    print(f"Pão '{estoque[nome_pao]['nome']}' selecionado.")
    print("O que deseja atualizar?")
    print("1. Valor")
    print("2. Quantidade em estoque")

    escolha_atualizacao = input("Escolha uma opção: ")

    try:
        if escolha_atualizacao == "1":
            novo_valor = float(input("Digite o novo valor: "))
            if novo_valor >= 0:
                estoque[nome_pao]["valor"] = novo_valor
                print("Valor atualizado com sucesso!")
            else:
                print("Valor inválido.")
        elif escolha_atualizacao == "2":
            nova_qtd = int(input("Digite a nova quantidade em estoque: "))
            if nova_qtd >= 0:
                estoque[nome_pao]["estoque"] = nova_qtd
                print("Estoque atualizado com sucesso!")
            else:
                print("Quantidade inválida.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida. Digite um número.")


def cadastrar_localidade(bairros: dict) -> None:
    """Permite ao atendente cadastrar um novo bairro para entrega."""
    nome_bairro = input("Digite o nome do novo bairro (identificador): ").lower()
    if nome_bairro in bairros:
        print("Erro: O bairro já está cadastrado.")

    try:
        nome_completo = input("Digite o nome completo do bairro: ")
        valor_frete = float(input("Digite o valor do frete: "))
        if nome_bairro and valor_frete >= 0:
            bairros[nome_bairro] = {"nome": nome_completo, "frete": valor_frete}
            print(f"Localidade '{nome_completo}' cadastrada com sucesso!")
        else:
            print("Dados inválidos. O cadastro não foi realizado.")
    except ValueError:
        print("Entrada inválida. O valor do frete deve ser um número.")


def iniciar_programa():
    """Função que inicia o loop principal do programa de vendas."""
    dados = carregar_dados_padaria()
    atendente = dados["atendente"]
    paes_estoque = dados["paes"]
    bairros_frete = dados["bairros"]
    codigo_base = dados["codigo_venda_base"]

    while True:
        print(
            f"\n-- Bem-vindo(a) à Padaria 'O Desespero', sou o(a) atendente {atendente} --"
        )
        print("\n--- Menu Principal ---")
        print("1. Iniciar Venda")
        print("2. Gerenciar Produtos")
        print("3. Cadastrar Nova Localidade")
        print("4. Sair do Sistema")

        escolha_menu = input("Escolha uma opção: ")

        if escolha_menu == "1":
            pedido = processar_pedido(paes_estoque)
            if pedido is None:
                continue

            pao_escolhido, qtd_pedido, valor_compra, paes_estoque = pedido
            print(
                f"Seu pedido de {qtd_pedido} {pao_escolhido['nome']}s ficou em R$ {valor_compra:.2f}."
            )

            forma_retirada = input("É para 1: retirar ou 2: entregar? ")
            valor_frete = 0.0

            if forma_retirada == "2":
                entrega = calcular_frete(bairros_frete)
                if entrega is None:
                    continue
                bairro_entrega_key, valor_frete = entrega
                print(
                    f"Valor do frete para o bairro {bairros_frete[bairro_entrega_key]['nome']} é de R$ {valor_frete:.2f}"
                )
            elif forma_retirada != "1":
                print("Opção de retirada inválida.")
                continue

            dados_cliente = obter_dados_cliente()
            forma_pagamento = selecionar_forma_pagamento()

            valor_total = valor_compra + valor_frete
            codigo_venda_final = gerar_codigo_venda(codigo_base)
            dados["codigo_venda_base"] = codigo_venda_final

            print("\n--- Resumo da Compra ---")
            print(f"Cliente: {dados_cliente['nome']}")
            print(f"Valor dos pães: R$ {valor_compra:.2f}")
            print(f"Valor do frete: R$ {valor_frete:.2f}")
            print(f"Forma de pagamento: {forma_pagamento}")
            print(f"Valor total: R$ {valor_total:.2f}")
            print(f"Código da entrega: {codigo_venda_final}")
            print("--- Compra Concluída ---")

        elif escolha_menu == "2":
            print("\n--- Gerenciamento de Produtos ---")
            print("1. Cadastrar Novo Produto")
            print("2. Atualizar Produto Existente")
            escolha_produto = input("Escolha uma opção: ")

            if escolha_produto == "1":
                cadastrar_produto(paes_estoque)
            elif escolha_produto == "2":
                atualizar_produto(paes_estoque)
            else:
                print("Opção inválida.")

        elif escolha_menu == "3":
            cadastrar_localidade(bairros_frete)

        elif escolha_menu == "4":
            print("Saindo do sistema. Até a próxima!")
            break

        else:
            print("Opção de menu inválida.")


iniciar_programa()
