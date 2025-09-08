clientes = [
    {"nome": "Ana", "idade": 21, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carlos", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Diana", "idade": 45, "cidade": "Belo Horizonte"},
    {"nome": "Eduarda", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Fábio", "idade": 25, "cidade": "São Paulo"},
]


print("--- Lista de Clientes ---")
for cliente in clientes:
    nome = cliente["nome"]
    idade = cliente["idade"]
    print(f"Nome: {nome}, Idade: {idade}")

soma_idades = 0
total_clientes = 0

for cliente in clientes:
    soma_idades += cliente["idade"]

total_clientes = len(clientes)
idade_media = soma_idades / total_clientes
print(f"\nIdade média dos clientes: {idade_media:.2f} anos")

clientes_por_cidade = {}

for cliente in clientes:
    cidade = cliente["cidade"]
    if cidade in clientes_por_cidade:
        clientes_por_cidade[cidade] += 1
    else:
        clientes_por_cidade[cidade] = 1

print("\n--- Clientes por Cidade ---")
print(clientes_por_cidade)
