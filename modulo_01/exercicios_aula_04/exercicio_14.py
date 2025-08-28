texto = input("Digite um texto: ").lower()
proibidas = ["spoiler", "segredo"]

i = 0
while i < len(proibidas):
    palavra = proibidas[i]
    while palavra in texto:
        pos = texto.index(palavra)
        texto = texto[:pos] + "***" + texto[pos + len(palavra) :]
    i += 1

print("Texto filtrado:", texto)
