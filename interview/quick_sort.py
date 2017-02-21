lst = [1, 9, 0, 2, 5, 4, 6, 8, 7, 3]

def partition(lst, p, q):
    pivot = lst[q - 1]
    i = p
    for j in range(p, q - 1):
        if lst[j] < pivot:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i += 1
    lst[q - 1] = lst[i]
    lst[i] = pivot
    return i

def quick_sort(lst, p, q):
    if p < q:
        r = partition(lst, p, q)
        quick_sort(lst, p, r)
        quick_sort(lst, r + 1, q)

quick_sort(lst, 0, len(lst))
print lst
