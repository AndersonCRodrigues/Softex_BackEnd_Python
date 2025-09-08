pontuacao_jogadores = {
    "Alice": 50,
    "Bob": 75,
    "Charlie": 120,
}

print("--- Pontuações Iniciais ---")
print(pontuacao_jogadores)
print("-" * 30)

jogador_especifico = "Alice"
print(f"Simulando uma rodada de jogo para '{jogador_especifico}'.")

try:
    pontos_ganhos = int(input(f"Quantos pontos {jogador_especifico} ganhou? "))

    if jogador_especifico in pontuacao_jogadores:
        pontuacao_jogadores[jogador_especifico] += pontos_ganhos
        print(f"'{jogador_especifico}' ganhou {pontos_ganhos} pontos.")
        print(
            f"Nova pontuação de '{jogador_especifico}': {pontuacao_jogadores[jogador_especifico]}"
        )
    else:
        print(f"Erro: O jogador '{jogador_especifico}' não foi encontrado.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para os pontos.")

print("-" * 30)

print("--- Adicionar e Pontuar Novo Jogador ---")

try:
    novo_jogador = input("Digite o nome do novo jogador: ")
    pontuacao_inicial = int(input(f"Digite a pontuação inicial de '{novo_jogador}': "))

    pontuacao_jogadores[novo_jogador] = pontuacao_inicial
    print(f"'{novo_jogador}' adicionado com {pontuacao_inicial} pontos.")

    pontos_extras = int(
        input(f"Quantos pontos '{novo_jogador}' ganhou em uma rodada? ")
    )
    pontuacao_jogadores[novo_jogador] += pontos_extras
    print(f"Pontuação de '{novo_jogador}' atualizada.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a pontuação.")

print("-" * 30)

print("--- Pontuações Finais ---")
print(pontuacao_jogadores)
