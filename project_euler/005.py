"""Algorithm:
1. Find an upper bound by testing with all numbers from 1 to 20.
2.
"""

edl = range(1, 21) # evenly divisible list.
upper_bound = 232792560
for i in edl:
    print upper_bound / float(i)

