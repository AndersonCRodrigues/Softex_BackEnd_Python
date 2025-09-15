from banco_dados import banco_dados
from autenticar import autenticar_usuario
from clientes import cadastrar_cliente, listar_clientes
from menu import menu_operacoes

def programa_principal() -> None:
    """Inicia o programa principal do banco"""
    dados = banco_dados()

    while True:
        print("-- Terminal Bancário --")
        print("1- Acessar conta.")
        print("2- Listar clientes.")
        print("3- Cadastrar novo cliente.")
        print("4- Encerrar Atendimento.")

        opcao = input("Opção: ")

        if opcao == "1":
            acesso = False
            for _ in range(dados["tentavas_login"]):
                conta = input("Digite a sua conta corrente: ")
                senha = input("Digite a sua senha: ")
                acesso, usuario = autenticar_usuario(dados, conta, senha)

                if acesso:
                    menu_operacoes(usuario)
                    break
                else:
                    print("Conta ou senha inválida!")

        elif opcao == "2":
            listar_clientes(dados)
        elif opcao == "3":
            cadastrar_cliente(dados)
        elif opcao == "4":
            print("Encerrando atendimento do terminal.")
            break
        else:
            print("Opção inválida.")

programa_principal()