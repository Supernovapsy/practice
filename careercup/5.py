from sys import argv

def pairs_below_k(a, k):
    # Critical values: m = k - min(a), r = k // 2
    # Critical lists
    m = k - min(a)
    r = k / 2

    s = list() # all numbers in q > r.
    t = list() # all numbers in q <= r.
    for unique in dict().fromkeys(a).iterkeys():
        if unique <= m:
            if unique <= r:
                t.append(unique)
            else:
                s.append(unique)
    t.sort()
    s.sort()

    ret = [(t[i], t[j]) for i in xrange(len(t)) for j in xrange(i + 1, len(t))]
    progress = 0
    for se in reversed(s):
        for i in xrange(progress):
            ret.append((t[i], se))
        for i in xrange(progress, len(t)):
            if t[i] + se <= k:
                ret.append((t[i], se))
            else:
                progress = i
                break
        else:
            progress = len(t)
    return ret

answer = pairs_below_k([int(e) for e in argv[2:]], int(argv[1]))
print '%d elements' % (len(answer))
print answer
