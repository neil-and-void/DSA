'''
obs: the biggest perm we can create out of an array of numbers is descending order

idea 0: move right most to the left until it gets in front of a bigger num

idea 1: go through list from right to left and if current is biggert than next, swap, return
'''
def nextPermutation(nums):
    n = len(nums)
    for i in range(n-1, 0, -1):
        if nums[i - 1] < nums[i]:
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
            return

nums = [5,1,4,2,3]
nextPermutation(nums)
print(nums)

