lst = [1, 9, 0, 2, 5, 4, 6, 8, 7, 3]

# In-place.
def heap_sort(lst):
    build_max_heap(lst)
    for i in reversed(range(1, len(lst))):
        # Put the smallest at the back.
        tmp = lst[0]
        lst[0] = lst[i]
        lst[i] = tmp
        # Then, ensure that the front of the list is the maxmimum element again
        # by rebuilding the heap, but with 1 size smaller.
        max_heapify(lst, 0, i)

def build_max_heap(lst):
    for i in reversed(range((len(lst)) / 2)):
        max_heapify(lst, i, len(lst))

def max_heapify(lst, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= heap_size:
        return
    left_greater = lst[left] > lst[i]
    right_greater = False
    if right < heap_size:
        right_greater = lst[right] > lst[i]
    if left_greater and right_greater:
        if lst[left] > lst[right]:
            right_greater = False
        else:
            left_greater = False
    if left_greater:
        tmp = lst[i]
        lst[i] = lst[left]
        lst[left] = tmp
        max_heapify(lst, left, heap_size)
    elif right_greater:
        tmp = lst[i]
        lst[i] = lst[right]
        lst[right] = tmp
        max_heapify(lst, right, heap_size)

heap_sort(lst)
print lst
