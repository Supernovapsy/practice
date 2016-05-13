from sys import argv
# best_indices = None
# best_val = nums[0]
# for i in range(len(nums)):
#     s = 0
#     for j, num in reversed(range(i, len(nums))):
#         s += num
#         if s > best_val:
#
# nums[:i]
# j
# nums[:i + 1]
# nums[j:i]
# nums[j:i+1], nums[i:i+1]

def dp(nums):
    # In each iteration:

    # i is the current index representing the end fo the prefix.

    # c is the best index of the sum from nums[b:] where b
    # is less than i which gives the largest sum.
    # bcv is the best_candidate_val, i.e. sum(nums[b:].

    # best_indices is the best answer found so far, and best_val is the best
    # value found so far.

    # connecting the subproblems:
    # Given best_indices, best_val, candidate, bcv for nums[:i],
    # candidate, bcv = nums[:i+1], bcv + nums[i]
    #             OR = nums[i:i+1], nums[i]
    # depending on which one has the highr bcv.

    # Note: nums has at least 1 number; so, the base case can just be the
    # condition at the end of the first iteration of the loop

    # example: 3,-55, 8, 3: works.

    c, cv = 0, nums[0]
    b, bv = (0, 1), nums[0]
    for i in xrange(1, len(nums)):
        # Examining nums[:i+1]
        cv += nums[i]
        if nums[i] > cv:
            cv = nums[i]
            c = i
        if cv > bv:
            bv = cv
            b = (c, i + 1)
    return bv

print dp([int(e) for e in argv[1:]])
