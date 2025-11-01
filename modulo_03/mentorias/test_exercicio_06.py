from exercicio_06 import linhas_para_colunas


def test_coversao_matriz():
    entrada = [[1, 2, 3], [4, 5, 6]]
    saida = [[1, 4], [2, 5], [3, 6]]

    entrada_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    saida_2 = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    assert linhas_para_colunas(entrada) == saida
    assert linhas_para_colunas(entrada_2) == saida_2
