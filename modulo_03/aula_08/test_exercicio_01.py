from exercicio_01 import escolher
import random


def test_escolher(mocker):
    resultado_random = [1, 3, 4, 2, 3, 1]
    resultado_mock = mocker.patch(
        "random.randint",
        side_effect=resultado_random,
    )

    lista1 = [random.randint(1, 5) for _ in range(3)]
    lista2 = [random.randint(1, 5) for _ in range(3)]

    resultado = escolher(lista1, lista2)
    assert resultado == [1, 3]
    assert resultado_mock.call_count == 6
