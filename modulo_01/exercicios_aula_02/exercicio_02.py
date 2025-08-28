preco = float(input("Digite o preço do produto: "))
if preco > 100:
    desconto = preco * 0.10
    novo_preco = preco - desconto
    print(f"O novo preço com 10% de desconto é R$ {novo_preco:.2f}.")
else:
    print("Preço sem desconto.")
