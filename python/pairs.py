def find_pairs(nums, s):
    pairs = set()
    num_set = set(nums)
    for n in nums:
        complement = s - n
        if (complement, n) not in pairs and (n, complement) not in pairs:
            pairs.add((n, complement))
    return pairs


print find_pairs([3, 2, 5, 7, 3, 4, 5, 8, -1, 3, 2, 8, 5, 3, 5, 6, 3], 9)
