"""
Crie uma função que receba duas listas de números inteiros geradas
com random.
Retorne uma nova lista contendo apenas os elementos que estão presentes em
ambas as listas, sem repetição.
"""

import random


def juncao(lista_01: list[int], lista_02: list[int]) -> list[int]:
    conjunto_01 = set(lista_01)
    conjunto_02 = set(lista_02)
    resultado = conjunto_01.intersection(conjunto_02)
    return list(resultado)


# lista_01 = []
# lista_02 = []

# for _ in range(3):
#     lista_01.append(random.randint(1, 5))
#     lista_02.append(random.randint(1, 5))

# print(juncao(lista_01, lista_02))
