def count_replace(s):
    if not s:
        return s

    ret = list()
    prev_c = s[0]
    count = 1
    for c in s[1:]:
        if c == prev_c:
            count += 1
        else:
            ret.append("{}{}".format(count, prev_c))
            prev_c = c
            count = 1

    ret.append("{}{}".format(count, prev_c))

    return "".join(ret)

string = "aaaggbbbbc"
print count_replace(string)
string = ""
print count_replace(string)
string = "aaaa"
print count_replace(string)
string = "a"
print count_replace(string)
string = "string"
print count_replace(string)
