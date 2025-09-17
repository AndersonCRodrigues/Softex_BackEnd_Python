def contar_palavras(frase: str) -> int:
    """Conta o número de palavras em uma frase."""
    palavras = frase.split()
    return len(palavras)


def contar_vogais(frase: str) -> int:
    """Conta o número de vogais em uma frase."""
    vogais = "aeiouAEIOU"
    count = 0
    for char in frase:
        if char in vogais:
            count += 1
    return count


def contar_consoantes(frase: str) -> int:
    """Conta o número de consoantes em uma frase."""
    vogais = "aeiouAEIOU"
    count = 0
    for char in frase:
        if char.isalpha() and char not in vogais:
            count += 1
    return count


def verificar_palindromo(frase: str) -> bool:
    """Verifica se uma frase é um palíndromo."""
    frase_limpa = "".join(char.lower() for char in frase if char.isalpha())
    return frase_limpa == frase_limpa[::-1]


def analisar_sentenca(frase: str) -> dict | None:
    """Analisa uma frase e retorna um dicionário com os resultados."""
    if not isinstance(frase, str) or not frase.strip():
        print("Entrada inválida. Por favor, digite uma frase.")
        return None

    resultado = {
        "total_palavras": contar_palavras(frase),
        "total_vogais": contar_vogais(frase),
        "total_consoantes": contar_consoantes(frase),
        "eh_palindromo": verificar_palindromo(frase),
    }
    return resultado


sentenca: str = input("Digite uma frase para analisar: ")
analise = analisar_sentenca(sentenca)

if analise:
    print("\n--- Resumo da Análise ---")
    print(f"Palavras: {analise['total_palavras']}")
    print(f"Vogais: {analise['total_vogais']}")
    print(f"Consoantes: {analise['total_consoantes']}")
    print(f"Palíndromo: {'Sim' if analise['eh_palindromo'] else 'Não'}")
