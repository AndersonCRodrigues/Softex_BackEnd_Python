senha_secreta = "abc123"
tentativas = 0
while tentativas < 3:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_secreta:
        print("Login bem-sucedido!")
        break
    else:
        print("Senha incorreta.")
    tentativas += 1
else:
    print("Tentativas esgotadas!")
