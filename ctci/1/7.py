import numpy as np

def print_matrix(matrix):
    for arr in matrix:
        print " ".join([str(ele) for ele in arr])

def selective_reset(matrix):
    M = len(matrix)
    N = len(matrix[0])

    zeroes = dict()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                zeroes[i + 1] = True
                zeroes[-j - 1] = True

    for rowcol in zeroes.keys():
        if rowcol > 0:
            matrix[rowcol - 1, :] = [0 for i in range(N)]
        else:
            matrix[:, -(rowcol + 1)] = [0 for i in range(M)]

matrix = [range(i, i + 10) for i in range(-5, 4)]
matrix = np.array(matrix)
print_matrix(matrix)
selective_reset(matrix)
print_matrix(matrix)
