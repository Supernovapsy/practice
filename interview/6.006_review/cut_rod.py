from sys import argv
length = int(argv[1])
price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

"""
1. subproblem:
optimal way of cutting a rod of length 1..n
2. guess:
next cut at 0..i
3. connect:
optimal of i = i OR 1 + optimal(i - 1) OR ...
4. memoize & recurse:
p[n] list to store optimal(i)
5. solve original problem:
get p[n - 1]

time complexity: # of subproblems * time per subproblem
n * (i)
n^2 = 1 + 2 + 3 + .. + n
"""

size = length + 1
p = [-1] * size
p[0] = price[0]
p[1] = price[1]
best_cuts = ["place_holder"] * size
best_cuts[0] = []
best_cuts[1] = []

def dp(n):
    if p[n] != -1:
        return p[n]
    # Guess the next best cut.
    p[n] = price[n]
    max_i = 0
    for i in range(1, n):
        candidate = price[i] + dp(n - i)
        if candidate > p[n]:
            p[n] = candidate
            max_i = i
    # Memoize the best cut.
    if max_i == 0:
        best_cuts[n] = []
    else:
        best_cuts[n] = [max_i] + [e + max_i for e in best_cuts[n - max_i]]
    return p[n]

dp(length)

print "${}: {}".format(p[-1], best_cuts[-1])
