from copy import deepcopy

e = [5, 4, [3, 2, 1]]
n = 10

out = list()

for j, new in enumerate(deepcopy(e) for i in xrange(n)):
    print new
    new.append(j)
    out.append(new)


print out
