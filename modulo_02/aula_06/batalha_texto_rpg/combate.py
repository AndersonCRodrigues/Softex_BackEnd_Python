import time


def batalha(heroi, monstro):
    while heroi.esta_vivo() and monstro.esta_vivo():
        print(f"\nVida do Herói: {heroi.vida} | "
              f"Vida do Monstro: {monstro.vida}")

        print("\nEscolha sua ação:")
        print("1) Atacar")
        print("2) Fugir")
        print("3) Usar Poção")
        print("4) Defender")
        escolha = input("Digite o número da ação: ")

        if escolha == "1":
            heroi.atacar(monstro)
        elif escolha == "2":
            print(f"{heroi.nome} fugiu da batalha!")
            break
        elif escolha == "3":
            heroi.usar_pocao()
        elif escolha == "4":
            heroi.defender()
            print(f"{heroi.nome} está defendendo no próximo ataque!")
        else:
            print("Escolha inválida! O turno foi perdido.")

        if not monstro.esta_vivo():
            print("O Herói venceu!")
            break

        time.sleep(1)
        monstro.atacar(heroi)

        if not heroi.esta_vivo():
            print("O Monstro venceu!")
            break

        time.sleep(1)
