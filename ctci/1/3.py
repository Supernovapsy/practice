def print_matrix(matrix):
    for arr in matrix:
        print " ".join([str(ele) for ele in arr])

def rotate_clockwise(matrix):
    N = len(matrix)
    for i in range(N / 2):
        layerN = N - i * 2
        start = i
        end = layerN + i - 1
        for j in range(layerN - 1):
            swap = matrix[start + j][end]
            matrix[start + j][end] = matrix[start][start + j]
            matrix[start][start + j] = matrix[end - j][start]
            matrix[end - j][start] = matrix[end][end - j]
            matrix[end][end - j] = swap

matrix = [range(i, i + 10) for i in range(10)]
print_matrix(matrix)
rotate_clockwise(matrix)
print_matrix(matrix)
