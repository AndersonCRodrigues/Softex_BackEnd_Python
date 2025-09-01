# exercicio 02
lista1 = ["vermelho", "azul", "verde", "amarelo"]
lista2 = ["verde", "roxo", "azul", "preto"]
elementos_comuns = []

for item in lista1:
    if item in lista2 and item not in elementos_comuns:
        elementos_comuns.append(item)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Elementos em comum: {elementos_comuns}")
