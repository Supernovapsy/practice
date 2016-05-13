def add_arrays(a1, a2):
    ret = list()
    carry = 0
    for i in xrange(min(len(a1), len(a2))):
        ret.append((a1[i] + a2[i] + carry) % 10)
        carry = (a1[i] + a2[i] + carry) / 10
    if len(a1) >= len(a2):
        a = a1
    else:
        a = a2
    for i in xrange(min(len(a1), len(a2)), len(a)):
        ret.append((a[i] + carry) % 10)
        carry = (a[i] + carry) / 10

    if carry == 1:
        ret.append(carry)
    return ret


a1 = [3, 6, 3]
a2 = [2, 4, 7, 8]

# 363 + 8742 = 9105
print ''.join(str(d) for d in reversed(add_arrays(a1, a2)))
