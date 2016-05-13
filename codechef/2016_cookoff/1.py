"""
N Apples
M oranges
apples == oranges
minimum number of differences between both fruits.

1 apple or 1 orange for 1 coin
k coins
"""

import sys

caseN = int(sys.stdin.readline())

for i in range(caseN):
    appleN, orangeN, k = [int(e) for e in sys.stdin.readline().split()]
    diff = abs(orangeN - appleN)
    if diff >= k:
        print diff - k
    else:
        print 0
