minha_tupla = (1, 2, 3, 4, 2)

minha_tupla.count(2) # Resultado: 2

minha_tupla.index(3) # Resultado: 2


lista = [1,2,3,4]
tupla = tuple(lista)
print(f"tupla {tupla}")
lista = list(tupla)
print(f"lista {lista}")

pessoas = [("Ana", 25), ("Bruno", 30), ("Carlos", 28),]

for nome, idade in pessoas:
    print(f"{nome} tem {idade} anos.")

# for item in pessoas:
#     print(item)