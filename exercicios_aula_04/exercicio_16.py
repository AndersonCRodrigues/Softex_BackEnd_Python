texto = input("Digite uma palavra ou frase: ").lower()
texto = texto.replace(" ", "")

invertido = ""
i = len(texto) - 1
while i >= 0:
    invertido += texto[i]
    i -= 1

if texto == invertido:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")
