# sum of all multiples of 3 and 5 under 1000.

sum = 0
for i in xrange(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum
