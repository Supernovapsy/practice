def soln(nums):
    N = len(nums)

    output = [1] * N

    for i in xrange(1, N):
        output[i] = nums[i - 1] * output[i - 1]
    top = 1
    for i in reversed(xrange(N - 1)):
        top = nums[i + 1 - N] * top
        output[i] *= top

    return output

nums = [1,2,3,4]

print soln(nums)
