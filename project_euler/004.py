"""Algorithm:
1. Compute all products of 3-digit numbers and store in list.
2. Sort them from biggest to smallest.
3. From biggest to smallest each check if it is a palindrome.
"""

def palindrome(n):
    for i in range(len(n) / 2):
        if n[i] != n[len(n) - 1 - i]:
            return False
    return True

numbers = [i * j for i in xrange(100, 1000) for j in xrange(100, 1000)]
numbers.sort()
for i in reversed(numbers):
    if palindrome(str(i)):
        print i
        break
