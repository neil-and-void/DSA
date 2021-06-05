'''
TODO: using a hashtable for quick look up, for each number check if the complement
      to that number exists
def twoSum(nums, target):
    create a map

    for each num in nums:
        check if the complement to that number exists in map
        if does exist
            return

        else
            add current number as (number: index) to map
'''

def twoSum(nums, target):
    complements = dict()
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]

        if complement in complements:
            return [i, complements[complement]]
        else:
            complements[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
res = twoSum(nums, target)
print(res)

