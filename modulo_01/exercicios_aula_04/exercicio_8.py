senha = input("Digite sua senha: ")

if senha.isalnum():
    print("Senha válida")
else:
    print("Senha inválida (use apenas letras e números)")
