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

# Nomes dos paes
nome_frances = "Frances"
nome_doce = "Doce"
nome_forma = "Forma"

# Valores dos paes
valor_frances = 0.50
valor_doce = 5.00
valor_forma = 5.99

# quantidade dos paes
quantidade_frances = 15
quantidade_doce = 20
quantidade_forma = 18

# nome do atendente
nome_atendente = "Maria"

# nome bairros
bairro_barroco = "barroco"
bairro_sao_jose = "sao jose"

# valores frentes
frete_barroco = 5.00
frete_sao_jose = 15.00

# código venda
codigo_venda = 98568

while True:
    print(f"-- Bem vindo a padaria Desespero, sou a atendente {nome_atendente}")
    escolha = input(f"Temos os pães: {nome_frances, nome_doce, nome_forma}. Qual pão você deseja?")
    if escolha == nome_frances:
        quantidade = int(input("Qual a quantidade?"))
        if quantidade <= quantidade_frances:
            quantidade_frances -= quantidade
            pedido_de_paes = quantidade
            valor_compra = quantidade * valor_frances
            print(f"Seu pedido ficou em R$ {valor_compra}.")
        else:
            print(f"Infelizmente só tenho {quantidade_frances} pães no momento!")
            break

    forma_retirada = input("É para 1: retirar ou 2: entregar?")
    if forma_retirada == "2":
        bairro_entrega = input(f"Qual o bairro? (1:{bairro_barroco},2:{bairro_sao_jose})")
        if bairro_entrega == "1":
            valor_frete = frete_barroco
            print(f"Valor do frete R$ {valor_frete}")
        elif bairro_entrega == "2":
            valor_frete = frete_sao_jose
            print(f"Valor do frete R$ {valor_frete}")
        else:
            print("Fora da área de entrega")
            break
    elif forma_retirada == "1":
        valor_frete = 0.00
    else:
        break

    dados_cliente = input("Infome seu nome: ")
    forma_pagamento = input("Escolha a forma de pagamento (1-dinheiro, 2-cartão): ")

    if forma_pagamento == "1":
        forma_pagamento = "Dinheiro"
    else:
        forma_pagamento = "Cartão"

    codigo_atual = codigo_venda + 1

    print(f'O valor todal da sua compra foi de R$ {valor_compra + valor_frete} com código {codigo_atual}')
    break