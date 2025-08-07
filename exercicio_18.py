n = int(input("Digite um número para calcular o fatorial: "))
if n < 0:
    print("Fatorial não existe para números negativos.")
else:
    fatorial = 1
    i = 1
    while i <= n:
        fatorial *= i
        i += 1
    print(f"O fatorial de {n} é: {fatorial}")
