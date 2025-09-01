# exercicio 03
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

for numero in numeros:
    eh_primo = True
    if numero < 2:
        eh_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                eh_primo = False
                break

    if eh_primo:
        primos.append(numero)

print(f"Lista original: {numeros}")
print(f"Números primos na lista: {primos}")
