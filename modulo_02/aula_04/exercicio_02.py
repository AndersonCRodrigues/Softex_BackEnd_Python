def adicionar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a: float, b: float) -> float | str:
    """Retorna a divisão de dois números, tratando a divisão por zero."""
    if b == 0:
        return "Erro! Divisão por zero não é permitida."
    return a / b


def menu_calculadora():
    """Exibe o menu da calculadora e coordena as operações."""
    while True:
        print("\n=== CALCULADORA ===")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")

        escolha = input("Escolha a operação: ")

        if escolha == "5":
            print("Saindo da calculadora. Até logo!")
            break

        if escolha in "1234":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if escolha == "1":
                    print(f"Resultado: {adicionar(num1, num2)}")
                elif escolha == "2":
                    print(f"Resultado: {subtrair(num1, num2)}")
                elif escolha == "3":
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif escolha == "4":
                    resultado_divisao = dividir(num1, num2)
                    print(f"Resultado: {resultado_divisao}")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")


menu_calculadora()
