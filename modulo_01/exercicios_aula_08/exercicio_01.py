senha_correta = "senha123"

while True:
    senha_digitada = input("Digite a senha para acessar o sistema: ")
    if senha_digitada == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")

while True:
    email_validacao = input(
        "Digite um e-mail para validação (ou 'sair' para encerrar): "
    )

    if email_validacao.lower() == "sair":
        print("Encerrando o programa.")
        break

    if "@" in email_validacao and email_validacao.endswith(".com"):
        print("E-mail válido!")
    else:
        print("E-mail inválido.")
