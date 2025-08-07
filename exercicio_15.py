while True:
    email = input("Digite um e-mail: ")
    if "@" in email:
        print("E-mail válido.")
        break
    else:
        print("E-mail inválido. Digite novamente.")
