import unittest

class binary_search_test(unittest.TestCase):
    def test1(self):
        test1 = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
        self.assertEqual(binary_search_with_empty_strings(test1, 'ball'), 4)

    def test2(self):
        test2 = ['at', '', '', '', '', 'ball', 'car', '', '', 'dad', '', '']
        self.assertEqual(binary_search_with_empty_strings(test2, 'ballcar'), -1)

def binary_search_with_empty_strings(a, e):
    i = 0
    j = len(a) - 1
    offset = 0 # The number of elements to the left or right of mid which is being searched.
    side = 1 # Whether left or right is going to be searched for the non-empty string.
    while j >= i:
        mid = i + (j - i) / 2 + offset * side
        if mid < i or mid > j:
            return -1
        else:
            if not a[mid]: # If the string is empty
                offset += (side + 1) / 2
                side *= -1
            else:
                if a[mid] == e:
                    return mid
                elif a[mid] > e:
                    j = mid - 2 * offset * side - 1 if side == 1 else mid -1
                elif a[mid] < e:
                    i = mid - 2 * offset * side if side == -1 else mid + 1
                offset = 0
                side = 1
    return -1

unittest.main()
