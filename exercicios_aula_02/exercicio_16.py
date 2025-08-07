import random

numero_secreto = random.randint(1, 100)  # Gera um número aleatório
tentativas = 0
print("Adivinhe o número secreto entre 1 e 100.")
while True:
    try:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("O número secreto é maior.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
