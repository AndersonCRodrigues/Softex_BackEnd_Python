numero = int(input("Digite um número inteiro positivo: "))
if numero == 0:
    print("0")
else:
    binario = ""
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero //= 2
    print(binario)
