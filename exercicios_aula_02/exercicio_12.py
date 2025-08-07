soma = 0
contador = 0
while contador < 5:
    numero = int(input(f"Digite o {contador + 1}º número: "))
    soma += numero
    contador += 1
print(f"A soma total é: {soma}")
