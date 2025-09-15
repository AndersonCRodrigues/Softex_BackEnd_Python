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