from sys import argv

def find_peak_1d(a):
    # i, j to keep track of bounds, and k to store which index to check.
    i, j = 0, len(a)

    if j == i:
        return None

    while True:
        if j - i == 1:
            return i
        k = (j - i) / 2 + i
        ele = a[k]
        left = a[k - 1]
        right = a[k + 1]

        if k == 0 and right <= ele:
            return k
        elif k == len(a) and left <= ele:
            return k
        elif ele >= left and ele >= right:
            return k
        elif ele < left:
            j = k
        else:
            i = k + 1

a = [0, 1, 2, 6, 8, 10, 11, 9999999999]
# array = [int(e) for e in argv[1:]]
print a[find_peak_1d(a)]
