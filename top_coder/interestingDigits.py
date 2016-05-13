class interestingDigits(object):
    def digits(self, base):
        ret = []
        for i in range(2, base - 1):
            n = 0
        for j in range(base**3 / i):
            n += i
            if (n % base + n / base % base + n / base / base % base) % i != 0:
                break
        else:
            ret.append(i)
    	return tuple(ret)

a = set()
a.add(1)
print 1 not in a
