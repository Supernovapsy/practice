class TrieNode(object):
    def __init__(self, is_end=False):
        self.parent = None
        self.children = {}
        self.is_end = is_end
        self.size = 1

    def update_size(self):
        node = self
        while node:
            if node.is_end:
                node.size = 1
            else:
                node.size = 0
            for child in node.children.itervalues():
                node.size += child.size
            node = node.parent

    def add(self, letter):
        if letter not in self.children:
            self.children[letter] = TrieNode()
            self.children[letter].parent = self
        return self.children[letter]

def init():
    root = TrieNode()
    root.size = 0
    return root

def add(root, word):
    if not word:
        return
    node = root
    for l in word:
        node = node.add(l)
    node.is_end = True
    node.update_size()

def find(root, word):
    if not word:
        return root.size
    node = root
    for l in word:
        if l in node.children:
            node = node.children[l]
        else:
            return 0
    return node.size

root = init()
n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')

    if op == "add":
        add(root, contact)
    elif op == "find":
        print find(root, contact)
