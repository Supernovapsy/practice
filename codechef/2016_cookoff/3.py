"""
list to store values of each node, and a pointer to each node
tree structure to store the parent structure

mem to store fibonacci sequence modulo 10^9+7.
"""

import sys

mem = [0, 1, 1]
storage = []
mod = 10**9 + 7

def expand_mem(k):
    current_len = len(mem)
    for i in xrange(current_len, k + 1):
        mem.append((mem[i - 2] + mem[i - 1]) % mod)

class Node(object):
    def __init__(self, tag):
        self.tag = tag
        self.children = []
    def add_child(self, tag):
        self.children.append(tag)

def create_tree_structure(tags):
    """tags is a list of ints."""
    root = Node(1)
    storage.append([root, 0])

    storage.extend([[Node(i + 2), 0] for i in xrange(len(tags))])

    for i, tag in enumerate(tags):
        get(tag)[0].add_child(i + 2)

def get(tag):
    return storage[tag - 1]

def add(tag, k):
    expand_mem(k)
    get(tag)[1] = (query(tag) + mem[k]) % mod

def query(tag):
    return storage[tag - 1][1]

def update(tag, k):
    level = 0
    frontier = [tag]
    n = []
    while frontier:
        for u in frontier:
            n.extend(get(u)[0].children)
            add(u, k + level)
        frontier = n
        n = []
        level += 1

nodeN, opN = [int(e) for e in sys.stdin.readline().split()]
tag_list = [int(sys.stdin.readline()) for i in xrange(nodeN - 1)]
create_tree_structure(tag_list)
for i in xrange(opN):
    inst = sys.stdin.readline().split()
    if inst[0] == 'Q':
        print query(int(inst[1]))
    else:
        update(int(inst[1]), int(inst[2]))
