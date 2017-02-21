from collections import deque

def list_equals_deque(lst, deq):
    if len(lst) != len(deq):
        return False

    for i, e in enumerate(deq):
        if lst[i] != e:
            return False
    return True

def create_palindrome(s):
    lst = list(s)
    left = lst[:len(s) / 2]
    right = deque(reversed(lst[len(s) - len(s) / 2:]))

    even = False
    if len(left) + len(right) == len(s):
        even = True

    for i in xrange(len(s)):
        if list_equals_deque(left, right):
            return "".join(reversed(list(s[-i:]))) + s
        if even:
            left.pop()
            right.popleft()
        else:
            right.popleft()
            right.append(s[(len(s) - i) / 2])
        even = not even

    assert False, "should not happen. palindrome should be found by for statement above"

p = "ab"
print create_palindrome(p)
p = "abc"
print create_palindrome(p)
p = "a"
print create_palindrome(p)
