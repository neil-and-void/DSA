'''
idea: sort, iterate and check whether or not the next number is the same as the last
def findDuplicate(nums):
    n = len(nums)
    nums = sorted(nums)

    i = 0
    while i < n-1 and nums[i] != nums[i+1]:
        i += 1
    return nums[i]
'''

'''
idea: use the number at each index to count
def findDuplicate(nums):
    for i from 0 to n:
        toggle nums[nums[i]] sign
    find positive number and return that index + 1
'''

def findDuplicate(nums):
    n = len(nums)
    for i in range(n):
        nums[abs(nums[i])] = -nums[abs(nums[i])]

    for i in range(1, n):
        if nums[i] > 0:
            return i

nums = [2,2,2,2,2]
res = findDuplicate(nums)
print(res)

