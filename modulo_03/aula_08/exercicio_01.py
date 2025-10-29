"""
Crie uma função que receba duas listas de números inteiros geradas
com random.
Retorne uma nova lista contendo apenas os elementos que estão presentes em
ambas as listas, sem repetição.
"""

import random


def escolher(lista_01: list[int], lista_02: list[int]) -> list[int]:
    conjunto_01 = set(lista_01)
    conjunto_02 = set(lista_02)
    resultado = conjunto_01.intersection(conjunto_02)
    return list(resultado)


# lista1 = [random.randint(1, 5) for _ in range(3)]
# lista2 = [random.randint(1, 5) for _ in range(3)]

# lista1 = []
# for _ in range(3):
#     lista1.append(random.randint(1, 5))
# resposta = escolher(lista1, lista2)
# print(resposta)
