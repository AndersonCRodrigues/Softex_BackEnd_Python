while True:
    try:
        lA = float(input("Digite o valor do lado A: "))
        lB = float(input("Digite o valor do lado B: "))
        lC = float(input("Digite o valor do lado C: "))

        if lA > 0 and lB > 0 and lC > 0:
            if (lA < lB + lC) and (lB < lA + lC) and (lC < lA + lB):
                print("\nOs valores podem formar um triângulo.")

                if lA == lB == lC:
                    print("Tipo: Triângulo Equilátero.")
                elif lA == lB or lA == lC or lB == lC:
                    print("Tipo: Triângulo Isósceles.")
                else:
                    print("Tipo: Triângulo Escaleno.")
                break
            else:
                print("Erro: os valores não podem formar um triângulo.\n")
        else:
            print("Erro: os lados devem ser maiores que zero.\n")

    except ValueError:
        print(
            "Erro: \n"
            "entrada inválida! Digite apenas números (inteiros ou decimais).\n"
        )
