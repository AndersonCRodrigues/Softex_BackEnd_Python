frase_original = input("Digite uma frase: ")
frase_codificada = ""
frase_decodificada = ""

for letra in frase_original.lower():
    if letra == "a":
        frase_codificada += "1"
    elif letra == "e":
        frase_codificada += "2"
    elif letra == "i":
        frase_codificada += "3"
    elif letra == "o":
        frase_codificada += "4"
    elif letra == "u":
        frase_codificada += "5"
    else:
        frase_codificada += letra

print("Codificada:", frase_codificada)

for caractere in frase_codificada:
    if caractere == "1":
        frase_decodificada += "a"
    elif caractere == "2":
        frase_decodificada += "e"
    elif caractere == "3":
        frase_decodificada += "i"
    elif caractere == "4":
        frase_decodificada += "o"
    elif caractere == "5":
        frase_decodificada += "u"
    else:
        frase_decodificada += caractere

print("Decodificada:", frase_decodificada)

codificada = frase_original.lower().replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")
print("CODIFICADA COM REPLACE: ",codificada)