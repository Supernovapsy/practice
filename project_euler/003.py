import math

"""Algorithm:
1. Find 2 small factors of n.
2. Find all prime numbers less than or equal to the largest of the two factors.
3. Check from the highest to the lowest if any such number is a factor of n.
The first such number is the largest prime factor of n.
"""

def fermat_factor_helper(n):
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    b = math.sqrt(b2)
    # This should be enough to determine squareness given the size of the number.
    while True:
        if b % 1 == 0:
            break
        a += 1
        b2 = a * a - n
        old_b = b
        b = math.sqrt(b2)
        if b - old_b < 1:
            # Range to be tested by brute force.
            return False, math.ceil(b), math.floor(math.sqrt(n))
    return True, a - b, a + b

def eratosthenes_sieve(n):
    """Returns primes <= n in ascending list."""
    sieve = [False, True] * int(math.floor(n / 2.0 + 1))
    sieve[1] = False
    sieve[2] = True
    limit = int(math.floor(math.sqrt(n)))
    for i in xrange(3, limit):
        if sieve[i]:
            sieve_n = i * 2
            while sieve_n < len(sieve):
                sieve[sieve_n] = False
                sieve_n += i
    for i, v in enumerate(sieve):
        if v:
            sieve[i] = i
    return filter(None, sieve)

def trial_divide_largest_factor(n):
    limit = math.floor(math.sqrt(n))
    for i in reversed(xrange(2, limit)):
        if n // i * i == n:
            return i

def try1(n):
    success, value1, value2 = fermat_factor_helper(n)
    if success:
        primes = eratosthenes_sieve(value2)
        for i in reversed(primes):
            if n // i * i == n:
                return i
    else:
        raise NotImplemented

n = 600851475143
print try1(n)
