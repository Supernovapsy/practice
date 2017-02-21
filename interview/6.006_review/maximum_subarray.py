arr = [3, 6, 1, 7, -34, 2, 609, -5, 2, 6, 1, 132, 42, -133]

toy = [5, -3, 5]

def maximum_subarray(arr):
    i = len(arr) - 1
    j = len(arr)
    s = arr[-1]
    max_sum = s
    max_i = i
    max_j = j
    for k in reversed(range(len(arr) - 1)):
        if s > 0:
            s += arr[k]
            i -= 1
        else:
            s = arr[k]
            i = k
            j = k + 1
        if s > max_sum:
            max_sum = s
            max_i = i
            max_j = j

    return arr[max_i:max_j], max_sum

print maximum_subarray(toy)
print maximum_subarray(arr)
