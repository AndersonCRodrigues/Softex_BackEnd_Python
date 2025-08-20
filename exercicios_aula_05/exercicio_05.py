frase = input("Digite uma frase: ")
maiusculas = 0
minusculas = 0
espacos = 0
for caractere in frase:
    if "a" <= caractere <= "z":
        minusculas += 1
    elif "A" <= caractere <= "Z":
        maiusculas += 1
    elif caractere == " ":
        espacos += 1
print(f"Letras maiúsculas: {maiusculas}")
print(f"Letras minúsculas: {minusculas}")
print(f"Espaços em branco: {espacos}")
