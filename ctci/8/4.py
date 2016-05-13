from sys import argv

def add_characters(perm, characters, k):
    if k == len(characters):
        print "".join(perm)
    else:
        for i in range(len(perm)):
            if perm[i] != characters[k]:
                # Add a character before position k.
                add_characters(perm[:i] + [characters[k]] + perm[i:], characters, k + 1)
        add_characters(perm[:] + [characters[k]], characters, k + 1)

def perm_aux(perm, characters_left, duplicate_list):
    for i, c in enumerate(characters_left):
        perm_aux(perm + [c], characters_left[:i] + characters_left[i + 1:],
        duplicate_list)
    if not characters_left:
        add_characters(perm, duplicate_list, 0)

def permutations(string):
    count = dict()
    for c in string:
        count[c] = count.get(c, 0) + 1
    uniques = [c for c in count.keys() if count[c] == 1]
    duplicates = [c for c in count.keys() if count[c] > 1 for i in range(count[c])]
    perm_aux([], uniques, duplicates)

permutations(argv[1])
