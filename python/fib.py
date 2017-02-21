import sys

def fib_dp(n):
    a = 0
    b = 1
    for i in xrange(n):
        tmp = a + b
        a = b
        b = tmp
    return a

n = int(sys.argv[1])
print fib_dp(n)
