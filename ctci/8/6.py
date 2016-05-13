from sys import argv
import random

def print_matrix(matrix):
    for a in matrix:
        print " ".join([str(ele) for ele in a])

def fill_aux(screen, m, n, coord, old_color, tobefilled):
    stack = [coord]
    while stack:
        x, y = stack.pop()
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) not in tobefilled and i >= 0 and i < m and j >= 0 and j < n and screen[i][j] == old_color:
                    tobefilled.add((i, j))
                    stack.append((i, j))
    return tobefilled

def fill(screen, coord, new_color):
    """Assumes that screen is an mxn rectangular matrix."""
    m = len(screen)
    if m == 0:
        return
    n = len(screen[0])
    tobefilled = fill_aux(screen, m, n, coord, screen[coord[0]][coord[1]], {coord})
    # Fill them with the color wanted.
    for i, j in tobefilled:
        screen[i][j] = new_color

matrix = [[random.randrange(3) for i in range(10)] for j in range(5)]
print_matrix(matrix)
print
fill(matrix, (3, 5), 3)
print_matrix(matrix)
