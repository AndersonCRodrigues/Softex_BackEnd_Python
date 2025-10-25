"""
Crie uma função que receba uma lista e dois índices:
início e fim. A função deve retornar o fatiamento (slice)
da lista, mesmo que o índice final seja menor que o inicial, simulando
um acesso circular
"""


def funcao(lista, idx_1, idx_2):

    tamanho = len(lista)
    if tamanho == 0:
        return []

    inicio = idx_1 % tamanho
    fim = idx_2 % tamanho

    lista[inicio:fim]

    if inicio <= fim:
        return lista[inicio:fim]
    else:
        parte_inicial = lista[inicio:]
        parte_final = lista[:fim]
    return parte_inicial + parte_final
