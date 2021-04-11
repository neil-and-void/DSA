'''
**********
VERY IMPORTANT THING LEARNED HERE:
sometimes the recurrence relation or table we are building in the
dynamic programming problem is not the actual problem we are trying to
solve, but an adjacent value that helps us achieve the overall problem
**********


idea: generate all subarrays and compare globalmax
def maxSubArray(nums):
    globalMax = negative infinity
    for i from 0 to n - 1
        sumFromI = 0
        for j from i to n - 1
            add nums[j] to sumFromI
        take max of sumFromI and globalMax
    return global max

idea: for each i, find the max sub ending at i, and then out of all of those find the max
def maxSubArray(nums):
    globalMax = [-inf]

    maxSubEndingAt(n, nums, globalMax)

def maxSubEndingAt(n, nums, globalMax):
    base n = 1
        globalMax = nums[0]
        returns nums[0]

    recursive
        globalMax = max of the bottom or globalmax
        return max of maxSubEndingAt(n - 1, nums) + nums[n] or num[n]


idea: no need to recurse, build from bottom with a table
def maxSubArray(nums):
    maxSubEndingAt = create list of 0's length n

    #base case
    make the first value in maxSubEndingAt = nums[0]

    globalMax = -inf

    # iterative case
    for i from 1 to n-1
        maxSubEndingAt[i] = max(maxSubEndingAt[i - 1] + nums[i], nums[i])
        globalMax = max(maxSubEndingAt[i], global)

    return global max


'''
# idea: for each i, find the max sub ending at i, and then out of all of those find the max
#def maxSubArray(nums):
#    globalMax = [float('-inf')]
#    idx = len(nums) - 1
#
#    maxSubEndingAt(idx, nums, globalMax)
#
#    return globalMax[0]


def maxSubEndingAt(idx, nums, globalMax):
    # base
    if idx == 0:
        globalMax[0] = nums[0]
        return nums[0]

    # recursive
    elif idx > 0:
        localMax = max(maxSubEndingAt(idx - 1, nums, globalMax) + nums[idx], nums[idx])
        globalMax[0] = max(localMax, globalMax[0])
        print(idx, localMax, globalMax)
        return localMax

# recursive, somewhat dynamic programming approach
def maxSubArray(nums):
    n = len(nums)
    maxSubEndingAt = [0 for i in range(n)]

    # base case
    maxSubEndingAt[0] = nums[0]

    globalMax = float('-inf')

    for i in range(n):
        maxSubEndingAt[i] = max(maxSubEndingAt[i-1] + nums[i], nums[i])
        globalMax = max(globalMax, maxSubEndingAt[i])

    return globalMax

nums = [5,4,-1,7,8]
print(maxSubArray(nums))

