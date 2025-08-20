altura = int(input("Digite a altura do triângulo: "))
for i in range(altura):
    linha = ""
    for j in range(i + 1):
        linha += "*"
    print(linha)
