from saldo import verificar_saldo, sacar_valor, depositar_valor
import boletos
from clientes import alterar_senha

def menu_operacoes(usuario: dict) -> None:
    """Exibe o menu de operações e executa a escolha do usuário autenticado"""
    while True:
        print(f"Bem-vindo, {usuario["nome"]}! ")
        print("Escolha uma opção: ")
        print("1- Ver saldo.")
        print("2- Sacar valor.")
        print("3- Depositar.")
        print("4- Pagar bolero.")
        print("5- Alterar Senha.")
        print("6- Sair.")

        opcao = input("Opção: ")

        if opcao == "1":
            verificar_saldo(usuario)
        elif opcao == "2":
            sacar_valor(usuario)
        elif opcao == "3":
            depositar_valor(usuario)
        elif opcao == "4":
            boletos.pagar_boleto(usuario)
        elif opcao == "5":
            alterar_senha(usuario)
        elif opcao == "6":
            print("Atendimento Finalizado.")
            break
        else:
            print("Opção inválida!")
