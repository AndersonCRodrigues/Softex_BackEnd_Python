estoque_principal = [
    ("Camiseta", 101),
    ("Calça", 102),
    ("Boné", 103),
    ("Tênis", 104),
]
estoque_online = [
    ("Boné", 103),
    ("Camisa Polo", 105),
    ("Calça", 102),
    ("Chinelo", 106),
]

set_principal = set(estoque_principal)
set_online = set(estoque_online)

em_ambos = set_principal.intersection(set_online)
print("Produtos disponíveis na loja e no site:")
print(em_ambos)

apenas_loja = set_principal.difference(set_online)
print("\nProdutos disponíveis apenas na loja física:")
print(apenas_loja)

apenas_online = set_online.difference(set_principal)
print("\nProdutos disponíveis apenas no site:")
print(apenas_online)
