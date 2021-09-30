'''
obs: the biggest perm we can create out of an array of numbers is descending order

idea 0: move right most to the left until it gets in front of a bigger num

idea 1: go through list from right to left and if current is biggert than next, swap, return
'''
def nextPermutation(nums):
    n = len(nums)

    decreasing = -1
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            decreasing = i-1
            break

    minBiggest = 0
    for i in range(n-1, -1, -1):
        if nums[decreasing] < nums[i]:
            minBiggest = i
            break

    # swap 
    temp = nums[decreasing]
    nums[decreasing] = nums[minBiggest]
    nums[minBiggest] = temp

    decreasingSubarrayLen = n - decreasing - 1
    for i in range(decreasingSubarrayLen // 2):
        temp = nums[decreasing + 1 + i]
        nums[decreasing + 1 + i] = nums[n - i - 1]
        nums[n - i - 1] = temp



nums = [1,3,5,4,2]
print(nums)
print('###')
nextPermutation(nums)
print(nums)

