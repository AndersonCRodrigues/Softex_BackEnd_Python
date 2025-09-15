def calcula_frete(bairros_disponives: dict) -> tuple[str, float]:
    """Calcula o valor do frete com base no bairro de entrega"""
    print("Bairros para entrega")
    while True:
        for bairro in bairros_disponives.values():
            print(f"- {bairro["nome"]}" )
        
        bairro_entrega_nome = input("Qual o bairro de entrega?").lower()

        bairro_encontrado = ""

        for chave, bairro in bairros_disponives.items():
            
            if bairro["nome"].lower() == bairro_entrega_nome:
                bairro_encontrado = chave
                break
        
        if not bairro_encontrado:
            print("Bairro fora da área de entrega")
        else:
            frete = bairros_disponives[bairro_encontrado]["frete"]
            return bairro_entrega_nome, frete