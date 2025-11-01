"""
Dada uma lista de listas (matriz $N \times M$), crie uma função para transpor
a matriz (linhas viram colunas).
Use list comprehension aninhada.

"""


def linhas_para_colunas(matriz):
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]

    # matriz_original = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


entrada = [
    [1, 2, 3],
    [4, 5, 6],
]
saida = [
    [1, 4],
    [2, 5],
    [3, 6],
]

# print(matriz[0][0])
# print(linhas_para_colunas(matriz_original))


def faz_matriz(linhas: list[any], quant_l, quant_c) -> list:
    matriz = {}
    for i in range(quant_l):
        linha = linhas[i]
        # print(linha)
        for j in range(quant_c):  # (len(linha)):
            # print(linha[j])
            indice = (i, j)
            matriz.update({indice: linha[j]})
            # print(indice)
        # print(f"i={i} j={j} linha{i+1} {linha[i]}")
        # elemento={(i,j):linhas[i]}
        # print(elemento)
    return matriz


def faz_contramatriz(linhas: list[any], quant_l, quant_c) -> list:
    contramatriz = {}
    for i in range(quant_l):
        novalinha = linhas[i]
        for j in range(quant_c):
            # print(novalinha[j])
            indice = (j, i)
            contramatriz.update({indice: novalinha[j]})

    return contramatriz
