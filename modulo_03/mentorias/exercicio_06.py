"""
Dada uma lista de listas (matriz $N \times M$), crie uma função para transpor
a matriz (linhas viram colunas).
Use list comprehension aninhada.

"""


def linhas_para_colunas(matriz):
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]


matriz_original = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# print(matriz[0][0])
# print(linhas_para_colunas(matriz_original))

# for i in range(2):
#     print(i)
# resposta = [
#     [1,4],
#     [2,5],
#     [3,6]
# ]
