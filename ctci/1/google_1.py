def print_matrix(matrix):
    for arr in matrix:
        print " ".join([str(ele) for ele in arr])

def print_matrix_diagonally(matrix):
    M = len(matrix)
    N = len(matrix[0])
    for i in range(N + M - 1):
        for j in range(M):
            x = j
            y = i - j
            if x >= 0 and x < M and y >= 0 and y < N:
                print matrix[x][y]

matrix = [range(i, i + 10) for i in range(5)]

print_matrix(matrix)
print
print_matrix_diagonally(matrix)
