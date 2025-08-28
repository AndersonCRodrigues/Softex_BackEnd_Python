palavra = input("Digite uma palavra: ")
contador_vogais = 0
vogais = "aeiou"
for letra in palavra.lower():
    if letra in vogais:
        contador_vogais += 1
print(f"A palavra tem {contador_vogais} vogais.")
