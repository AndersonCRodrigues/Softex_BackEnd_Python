estoque_farmacia = {
    "paracetamol": {"preco": 5.50, "quantidade": 25},
    "ibuprofeno": {"preco": 8.90, "quantidade": 15},
    "vitamina C": {"preco": 12.00, "quantidade": 50},
}

while True:
    print("\n--- Sistema da Farmácia ---")
    print("1. Vender produto")
    print("2. Adicionar/atualizar produto")
    print("3. Listar estoque")
    print("4. Sair")

    try:
        escolha = input("Digite sua escolha: ")
        escolha = int(escolha)
    except ValueError:
        print("Entrada inválida. Digite um número de 1 a 4.")
        continue

    if escolha == 1:
        print("\n--- Venda ---")
        try:
            produto = input("Nome do produto: ").lower()
            quantidade_venda = int(input("Quantidade: "))

            if estoque_farmacia[produto]["quantidade"] >= quantidade_venda:
                estoque_farmacia[produto]["quantidade"] -= quantidade_venda
                print(f"Venda de {quantidade_venda} {produto} realizada.")
            else:
                print("Estoque insuficiente.")
        except KeyError:
            print("Produto não encontrado no estoque.")
        except ValueError:
            print("Quantidade inválida. Por favor, use números.")

    elif escolha == 2:
        print("\n--- Adicionar/Atualizar ---")
        try:
            produto = input("Nome do produto: ").lower()
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            if produto in estoque_farmacia:
                estoque_farmacia[produto]["quantidade"] += quantidade
                estoque_farmacia[produto]["preco"] = preco
                print(f"Estoque de {produto} atualizado.")
            else:
                estoque_farmacia[produto] = {"preco": preco, "quantidade": quantidade}
                print(f"Produto {produto} adicionado.")
        except ValueError:
            print("Entrada inválida. Preço e quantidade devem ser números.")

    elif escolha == 3:
        print("\n--- Estoque Atual ---")
        for produto, dados in estoque_farmacia.items():
            print(
                f"Produto: {produto} | Preço: R${dados['preco']:.2f} | Quantidade: {dados['quantidade']}"
            )

    elif escolha == 4:
        print("Saindo do sistema. Até logo!")
        break  # Sai do loop while e encerra o programa

    else:
        print("Opção não existe. Tente novamente.")
