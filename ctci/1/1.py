from sys import argv

def unique(string):
    return len(dict.fromkeys(string).keys()) == len(string)

print unique(argv[1])
