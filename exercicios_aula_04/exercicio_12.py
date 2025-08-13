texto = input("Digite um texto: ").lower()

vogais = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

i = 0
while i < len(texto):
    letra = texto[i]
    if letra in vogais:
        qtd_vogais += 1
    elif letra >= "a" and letra <= "z":
        qtd_consoantes += 1
    i += 1

print("Vogais:", qtd_vogais)
print("Consoantes:", qtd_consoantes)
