""" Lessons
1. .add(), .remove(), .update() do not return anything.
2. set() is not mutable, but frozen set is.
3. recursion combined with an intuition for the problem can be powerful.
"""

def all_subsets_aux(l, n):
    if n == 0:
        return {frozenset()}
    ret = set()
    for e in l:
        new_l = l[:]
        new_l.remove(e)
        subset_list = all_subsets_aux(new_l, n - 1)
        for subset in subset_list:
            new_subset = set(subset)
            new_subset.add(e)
            ret.add(frozenset(new_subset))
    return ret

def all_subsets(s):
    l = list(s)
    ret = set()
    for i in range(len(l) + 1):
        ret.update(all_subsets_aux(l, i))
    return ret

print all_subsets({1, 2, 3})
