"""
Crie uma função que receba uma lista de números e retorne a soma
máxima de qualquer sublista contígua (algoritmo de Kadane - Avançado).
use: função, for, if/else, max(), print
"""


def soma(lista):
    if not lista:
        return 0

    soma_maxima_global = lista[0]
    soma_maxima_local = lista[0]

    for num in lista[1:]:
        soma_maxima_local = max(num, soma_maxima_local + num)
        soma_maxima_global = max(soma_maxima_global, soma_maxima_local)

    return soma_maxima_global


lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(soma(lista))
