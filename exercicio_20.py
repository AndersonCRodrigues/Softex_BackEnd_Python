palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 5

while tentativas > 0 and "_" in letras_descobertas:
    print(" ".join(letras_descobertas))
    print(f"Você tem {tentativas} tentativas.")
    palpite = input("Digite uma letra: ").lower()

    if palpite in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == palpite:
                letras_descobertas[i] = palpite
    else:
        tentativas -= 1
        print("Letra não encontrada.")

if "_" not in letras_descobertas:
    print(f"Parabéns! Você descobriu a palavra: {''.join(letras_descobertas)}")
else:
    print(f"Suas tentativas acabaram. A palavra era: {palavra_secreta}")
