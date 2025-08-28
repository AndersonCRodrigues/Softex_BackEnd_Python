valor_hamburguer = 20.00
cupom_desconto = "123"

while True:
    lanche = input("Qual lanche você deseja? ")
    if lanche == "hamburguer":
        print("Pedido confirmado")
        break
    else:
        print("Este lanche não esta cadastrado, tente novamente. ")

cupom = input("Digite seu cupom de desconto: ")
if cupom == cupom_desconto:
    print(f"Seu lanche custou {valor_hamburguer * 0.9}")
else:
    print(f"Seu lanche custou {valor_hamburguer}")
