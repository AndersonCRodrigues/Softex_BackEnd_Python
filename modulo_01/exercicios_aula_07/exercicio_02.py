numero_secreto = 42

print("Bem-vindo ao jogo de adivinhação!")
print("Você tem 5 tentativas para adivinhar um número.")

for tentativa in range(5):
    palpite = int(input(f"Tentativa {tentativa + 1}: "))

    if palpite < numero_secreto:
        print("Muito baixo.")
    elif palpite > numero_secreto:
        print("Muito alto.")
    else:
        print("Parabéns! Você adivinhou o número.")
        break
else:
    print("Suas tentativas acabaram!")
    print(f"O número secreto era {numero_secreto}.")
