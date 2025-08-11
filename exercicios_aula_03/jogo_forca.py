palavra = "python"
tentativas = ""
erros = 0

print("=== Jogo da Forca Simples ===")

while erros < 6:
    exibicao = ""
    i = 0
    while i < len(palavra):
        if palavra[i] in tentativas:
            exibicao += palavra[i]
        else:
            exibicao += "_"
        i += 1
    print(exibicao)

    if "_" not in exibicao:
        print("Você ganhou! A palavra era:", palavra)
        break

    chute = input("Digite uma letra: ").lower()

    if len(chute) != 1:
        print("Digite apenas uma letra.")
    elif chute in tentativas:
        print("Você já tentou essa letra.")
    elif chute in palavra:
        print("Acertou!")
        tentativas += chute
    else:
        print("Errou!")
        tentativas += chute
        erros += 1

if erros == 6:
    print("Você perdeu! A palavra era:", palavra)
