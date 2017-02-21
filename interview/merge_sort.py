lst = [1, 9, 0, 2, 5, 4, 6, 8, 7, 3]

def merge_sort(lst, p, q):
    if q - p == 0:
        return []
    elif q - p == 1:
        return lst[p:q]
    middle = (q + p) / 2
    left = merge_sort(lst, p, middle)
    right = merge_sort(lst, middle, q)
    i = 0
    j = 0
    new = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    if i != len(left):
        new.extend(left[i:])
    else:
        new.extend(right[j:])
    return new

print len(lst)
print merge_sort(lst, 0, len(lst))
