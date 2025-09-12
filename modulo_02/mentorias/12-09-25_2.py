"""
25. Analisador de Texto: Crie uma função que receba
um texto e retorne um dicionário contendo a contagem de palavras,
a contagem de vogais e a contagem de consoantes.
"""


def conta_vogais(texto: str) -> int:
    """Conta o número de vogais de um texto"""
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if letra in vogais:
            contador += 1

    return contador


def conta_consoantes(texto: str) -> int:
    """Conta o número de consoantes de um texto"""
    vogais = "aeiou"
    contador = 0

    for letra in texto.lower():
        if (
            letra not in vogais
            and letra != " "
            and not letra.isdigit()
            and letra.isalpha()
        ):
            contador += 1

    return contador


def conta_palavras(texto: str) -> int:
    """Conta o número de palavras de um texto"""
    texto_lista = texto.split(" ")
    print(f"Texto em lista {texto_lista}")
    return len(texto_lista)


# texto = input("Entre com uma frase: ")
# total_vogais = conta_vogais(texto)
# total_consoante = conta_consoantes(texto)
# total_palavras = conta_palavras(texto)
# print(f"Total de vogais = {total_vogais}")
# print(f"Total de consoantes = {total_consoante}")
# print(f"O total de palavras no texto é de {total_palavras}")


def texto_dicionario(texto: str) -> dict:
    """
        Tranforma o dados do texto em um dicionario
        de vogais, consoantes e palavras
    """
    total_vogais = conta_vogais(texto)
    total_consoante = conta_consoantes(texto)
    total_palavras = conta_palavras(texto)

    return {
        "total_vogais": total_vogais,
        "total_consoante": total_consoante,
        "total_palavras": total_palavras,
    }


texto = input("Entre com uma frase: ")
dicionario = texto_dicionario(texto)
print(f"Os dados do texo são\n {dicionario}")
