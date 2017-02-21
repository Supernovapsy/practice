import sys

def longest_substring_unique(s):
    best_i = 0
    best_j = 0
    running_set = set()
    for i, c in enumerate(s):
        if c in running_set:
            if len(running_set) > best_j - best_i:
                best_i = i - len(running_set)
                best_j = i
            running_set = set()
        else:
            running_set.add(c)

    # corner case: running set can run until the end of the string.
    if len(running_set) > best_j - best_i:
        return s[-len(running_set):]

    return s[best_i:best_j]

s = "afiweiffijafewjafjijdsijfaj"
s = "zbasdqwerpoijbmkcma;kwuetjypoijvahsairje;oaijasohirqjefdj;"
s = "abcdefghijklmnopqrstuvwxyz"

print longest_substring_unique(s)
