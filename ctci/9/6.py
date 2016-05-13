import unittest

class test_6(unittest.TestCase):
    def test1(self):
        test = ((65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110))
        print dp(test, 0, [])[1]
        self.assertEqual(dp(test, 0, [])[0], 6)

def dp(a, i, tower):
    if i == len(a):
        return len(tower), tower
    no = dp(a, i + 1, tower)
    yes = no
    for j in range(len(tower) - 1):
        if tower[j][0] > a[i][0] and tower[j + 1][0] < a[i][0] and tower[j][1] > a[i][1] and tower[j + 1][1] < a[j][1]:
            yes = dp(a, i + 1, tower[:j + 1] + [a[i]] + tower[j + 1:])
            break
    else:
        if len(tower) == 0 or (tower[-1][0] > a[i][0] and tower[-1][1] > a[i][1]):
            yes = dp(a, i + 1, [a[i]] + tower[:])
        elif tower[0][0] < a[i][0] and tower[0][1] < a[i][1]:
            yes = dp(a, i + 1, [a[i]] + tower[:])
    return yes if yes[0] > no[0] else no

unittest.main()
