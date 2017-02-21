def sort_by_freq(a):
    count = dict()
    neg_firsts = dict()
    for i, c in enumerate(a):
        if c not in neg_firsts:
            neg_firsts[c] = -i
        count[c] = count.get(c, 0) + 1

    unsorted = list()
    for c in neg_firsts.iterkeys():
        # Each tuple is of the form (count, -<first index>)
        unsorted.append((count[c], neg_firsts[c]))
    unsorted.sort(reverse=True)

    # Need to negate the index to get the actual value.
    ret = [a[-tup[1]] for tup in unsorted]
    return ret

a = [5, 2, 3, 4, 1, 7, 4, 7,8, 4,2 ,5 ,6 ,6 ,7 ,3, 3, 2, 8, 2, 5]
print sort_by_freq(a)
a = []
print sort_by_freq(a)
a = [3]
print sort_by_freq(a)
a = [3, 3]
print sort_by_freq(a)
a = [3, 0]
print sort_by_freq(a)
a = [3, 0, 0]
print sort_by_freq(a)
