frutas = {"maçã", "banana", "laranja"}

# Duplicatas são automaticamente removidas
frutas = set(["maçã", "banana", "laranja", "banana"])

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))                 # {1, 2, 3, 4, 5}
print(A.intersection(B))          # {3}
print(A.difference(B))            # {1, 2}
print(A.symmetric_difference(B))  # {1, 2, 4, 5}

frutas = {"maçã", "banana"}

frutas.add("laranja")     # Adiciona
frutas.remove("banana")   # Remove (erro se não existir)
frutas.discard("uva")     # Remove se existir (sem erro)

frutas = {"maçã", "banana", "laranja"}

for fruta in frutas:
    print(fruta)

produtos = {
    ("produto1", 10, 2.5),
    ("produto2", 5, 4.0),
    ("produto3", 8, 3.25)
}

for nome, qtd, preco in produtos:
    total = qtd * preco
    print(f"{nome}: {qtd} unidades x R${preco:.2f} = R${total:.2f}")
