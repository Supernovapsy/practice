from sys import argv

def find_i_aux(a, i, j):
    """i and j are the beginning and end indices to search.

    This is given that between i and j, a breakpoint exists <=> a[j] < a[i]."""
    if j - i == 1:
        return j if a[j] < a[i] else None
    k = (j - i) / 2 + i
    if a[k] < a[i]:
        return find_i_aux(a, i, k)
    elif a[k] > a[i]:
        return find_i_aux(a, k, j)
    else: # a[k] == a[i]
        if a[j] < a[k]:
            return find_i_aux(a, k, j)
        else: # a[j] == a[k]
            t = find_i_aux(a, i, k)
            if t is not None:
                return t
            return find_i_aux(a, k, j)

def find_i(a):
    """Returns the breakpoint index between two sorted arrays merged into one
    array side by side."""
    if a[-1] <= a[0]:
        return find_i_aux(a, 0, len(a) - 1)
    return None

def binary_search(a, e, r):
    # r represents the number of rotations an increasing-sorted array has gone.
    offset = r - len(a)
    i = 0
    j = len(a) - 1
    while j >= i:
        k = (j - i) / 2 + i
        if a[k + offset] == e:
            return k + r
        elif a[k + offset] > e:
            j = k - 1
        else:
            i = k + 1
    return None

def find_element_in_rotated_sorted_array(a, e):
    if len(a) == 0:
        return None
    elif len(a) == 1:
        if a[0] == e:
            return 0
        return None
    i = find_i(a)
    i = i if i else 0
    return binary_search(a, e, i)

print find_element_in_rotated_sorted_array([int(i) for i in argv[1:]], 5)
