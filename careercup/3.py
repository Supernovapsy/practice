from sys import argv

def find_repeat(s):
    count = dict()
    for c in s:
        count[c] = count.get(c, 0) + 1

    pairs = set()
    for c, v in count.iteritems():
        if v > 2:
            return (c, c)
        elif v == 2:
            pairs.add(c)

    # Maps a character to its hash of characters.
    first = dict()
    last = dict()
    for c in s:
        if c in pairs:
            for d, h in last.iteritems():
                if c in h:
                    return (d, c)

            delete_from_first = False
            for d, h in first.iteritems():
                if c == d:
                    last[c] = h
                    delete_from_first = True
                else:
                    h.add(c)
            if delete_from_first:
                del first[c]

        if c not in first and c not in last:
            first[c] = {c}

    return None

print find_repeat(argv[1])
