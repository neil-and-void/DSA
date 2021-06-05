'''
idea 0: start from 0 and iterate and check if in array

idea 1: same as above but do it with a hashtable

idea 2: sort and check
    - check for the range of the array and determine which of the 3 cases it could be

idea 3: iterate with negative flag with similar approach to the sorting above
def firstMissingPositive(nums):
    min = of array
    max = of array

    if the min is greater than 1, return 1

    proccess the array to turn all negatives and 0's to inf

    for num in nums
        if abs(num) is in range of arr index
            change the sign of nums[num - 1] to negative

    iterate through array and return index + 1 of index of first positive number


    return maxNum + 1
'''

'''
implementation with supplementary array to get logic correct
def firstMissingPositive(nums):
    n = len(nums)
    minNum = min(nums)
    maxNum = max(nums)

    if minNum > 1 or maxNum < 0:
        return 1

    seen = [1 for i in range(n)]

    for num in nums:
        if num-1 in range(n):
            seen[num-1] = -1

    # find first negative
    for i in range(n):
        if seen[i] > 0:
            return i+1

    return maxNum + 1
'''

# implementation using no supplementary array
def firstMissingPositive(nums):
    n = len(nums)
    minNum = min(nums)
    maxNum = max(nums)

    if minNum > 1:
        return 1

    for i in range(n):
        if nums[i] <= 0:
            nums[i] = float('inf')

    for num in nums:
        absNum = abs(num)
        if absNum - 1 in range(n):
            nums[absNum - 1] = abs(nums[absNum - 1]) * -1

    # iterate through array and return index + 1 of index of first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return maxNum + 1

nums = [1]
ans = firstMissingPositive(nums)
print(ans)

