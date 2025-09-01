lista = [1,"1", 1.1, True, ["outra lista"]]

print(lista)
print(lista[0])

lista[0] = 2
print(lista[0])

print(len(lista))

for i in lista:
    print(i)

lista.append("ultimo valor")
print(lista)

item_removido = lista.pop()
print(lista)
print(item_removido)


