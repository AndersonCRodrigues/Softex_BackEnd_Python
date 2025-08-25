posicao = 0

while True:
    comando = input("Digite um comando\n"
                    "1- Avançar.\n"
                    "2- Recuar.\n"
                    "3- Mostrar status.\n"
                    "4- Desligar.\n" \
                    "Comando: ")
    if comando == "1":
        posicao += 1
    elif comando == "2":
        posicao -= 1
    elif comando == "3":
        print(f"Posição atual é {posicao}.")
    elif comando == "4":
        print("Desligand...")
        break
    else:
        print("Comando inválido!")