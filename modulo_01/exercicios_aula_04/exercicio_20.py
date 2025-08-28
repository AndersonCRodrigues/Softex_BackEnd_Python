nome = input("Digite seu nome completo: ").lower()

novo_nome = ""
i = 0

while i < len(nome):
    if i == 0 or nome[i - 1] == " ":
        novo_nome += nome[i].upper()
    else:
        novo_nome += nome[i]
    i += 1

espaco_final = novo_nome.rindex(" ")
ultimo_nome = novo_nome[espaco_final + 1:].upper()
novo_nome = novo_nome[: espaco_final + 1] + ultimo_nome

print("Nome formatado:", novo_nome)
