from sys import argv

def subsets(S):
    ret = set()
    listified = list(S)
    size = len(listified)
    for i in range(2**size):
        subset = set()
        for j in range(size):
            if i % 2 == 1:
                subset.add(listified[j])
            i //= 2 # Halve i in order to look at the next digit in the binary.
        ret.add(tuple(subset))
    return ret

S = {i for i in range(int(argv[1]))}
soln = subsets(S)
print soln
print "There are %d subsets in %r" % (len(soln), S)
print type(soln)
