# Sum of even fibonacci numbers below 4M.

sum = 0
a = 1
b = 2
four_mill = 4000000
while b <= four_mill:
    if b % 2 == 0:
        sum += b
    tmp = b
    b = a + b
    a = tmp

print sum
