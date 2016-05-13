def rot(string1, string2):
    two = string1 + string1
    return two.find(string2) != -1

print rot('waterbottle', 'erbottlewat')
print rot('waterbottle', 'erbottlewat')
