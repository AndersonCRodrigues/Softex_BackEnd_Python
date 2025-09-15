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

    paes_disponiveis[pao_encontrado]["quantidade"] -= quantidade
    valor_compra = quantidade * pao_escolhido["valor"]

    return pao_escolhido, quantidade, valor_compra, paes_disponiveis