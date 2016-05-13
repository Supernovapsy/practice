#!/bin/python

import sys

def turn(f, rem, balsa):
    if (f, rem, balsa) not in mem:
        if sum(f) == 0:
            mem[f, rem, balsa] = rem != 0 if balsa else rem == 0
        else:
            for i in range(3):
                if f[i] > 0:
                    d1 = list(f)
                    d1[i] -= 1
                    if balsa and not turn(tuple(d1), (rem + i) % 3, not balsa):
                        mem[f, rem, balsa] = True
                        break
                    elif not balsa and not turn(tuple(d1), (rem - i) % 3, not balsa):
                        mem[f, rem, balsa] = True
                        break
            else:
                mem[f, rem, balsa] = False
    return mem[f, rem, balsa]

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int,raw_input().strip().split(' '))
    # your code goes here
    mem = {}

    d = {0: 0, 1: 0, 2: 0}
    for e in a:
        d[e % 3] += 1
    if turn(tuple([d[m] for m in range(3)]), 0, True):
        print "Balsa"
    else:
        print "Koca"
