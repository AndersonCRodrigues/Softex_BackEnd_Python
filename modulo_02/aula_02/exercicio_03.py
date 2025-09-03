acessos = [
    ("Pedro", "sucesso"),
    ("Ana", "falha"),
    ("Maria", "sucesso"),
    ("Pedro", "falha"),
    ("Ana", "falha"),
]

usuarios_com_sucesso = set()
usuarios_com_falha = set()

for usuario, status in acessos:
    if status == "sucesso":
        usuarios_com_sucesso.add(usuario)
    elif status == "falha":
        usuarios_com_falha.add(usuario)

somente_falha = usuarios_com_falha.difference(usuarios_com_sucesso)

print("Usuários com pelo menos um login bem-sucedido:")
print(usuarios_com_sucesso)
print("\nUsuários que tiveram somente logins com falha:")
print(somente_falha)
