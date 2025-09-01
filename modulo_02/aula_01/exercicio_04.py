# exercicio 04
dados_validos = []
soma_total = 0

while True:
    entrada = input("Digite um número (ou -1 para parar): ")

    if entrada == "-1":
        print("Coleta de dados finalizada.")
        break

    if entrada.isdigit() or entrada.startswith("-") and entrada[1:].isdigit():
        numero = int(entrada)

        if 0 <= numero <= 100:
            dados_validos.append(numero)
            soma_total += numero
        else:
            print("Número fora do intervalo. Digite um valor entre 0 e 100.")
    else:
        print("Entrada inválida. Por favor, digite apenas números.")

print(f"\nSoma dos números válidos: {soma_total}")
print(f"Números coletados: {dados_validos}")
