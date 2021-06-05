'''
idea: dfs and backtrack once we get to a depth of 3 and target is reached
    - more specifically, have a search root and dfs on the right side of the list
      to prevent adding duplicates
    - as for improving our search space, back track once we have reached a candidate
      list of 3

def threeSum(nums):
    check that nums is greater or equal to 3
    candidate = []
    answers = []

    threeSumRec(nums, candidate, answers)

    return answers

def threeSumRec(nums, searchRoot, candidate, ans):
    # base
    if candidate length is 3 and sum of candidate is 0:
        add candidate to answers (make sure to make a new list)
        return

    # recursive
    for i from searchRoot to n-3:
        add nums[i] to candidate
        threeSumRec(nums, i)
        pop the end from candidate

# idea: build on two sum
def threeSum(nums):
    answers = []
    for each i from 0 to n:
        create a target by 0 - nums[i]

        for each j from i+1 to n:
            create complements hashtable
            get complement of nums[j]

TODO: build two sum first before making three sum
def twoSum(nums, target):
    create hashtable to hold complements
    for num in nums:
        complement = target - num
        does complement exist in complements

'''


'''
O(3^n) -ish solution, using dfs and backtracking
import copy
def threeSum(nums):
    if len(nums) < 3:
        return []
    candidate = set()
    ans = []
    searchRoot = 0

    threeSumRec(nums, searchRoot, candidate, ans)

    return ans

def threeSumRec(nums, searchRoot, candidate, ans):
    # base
    print(candidate)
    if len(candidate) > 3:
        return

    if len(candidate) == 3 and sum(candidate) == 0:
        newAns = copy.deepcopy(list(candidate))
        ans.append(newAns)
        return

    # recursive
    for i in range(searchRoot, len(nums)):
        if nums[i] not in candidate:
            candidate.add(nums[i])
            threeSumRec(nums, i+1, candidate, ans)
            candidate.remove(nums[i])
'''

'''
def threeSum(nums):
    nums = sorted(nums)
    n = len(nums)
    ans = []

    i = 0
    while i < n:
        target = 0 - nums[i]
        complements = dict()

        for j in range(i+1, n):
            complement = target - nums[j]
            if complement in complements:
                ans.append([nums[i], nums[j], nums[complements[complement]]])
            else:
                complements[nums[j]] = j

        while i < n - 1 and nums[i] == nums[i+1]:
            i += 1
        i +=1

    return ans
'''

'''
learned:
    - we should consider sorting if we know we are going to be at least n^2 without sorting
    - sorting can allow us to maintain non-repetive combinations
    - sorting an answer can allow us to basically have it be constant time and prevent
      duplicates
idea: iterate and create target for 2 sum with 2 pointers
def threeSum(nums):
    create answers map

    for i from 0 to n:
        target = 0 - nums[i]
        create complements map

        for j from i+1 to n
            complement = target - nums[j]

            if complement in complements
                add sorted tuple of values
            else
                add current num to complements
'''
def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    answers = set()

    for i in range(n):
        target = 0 - nums[i]
        complements = set()

        for j in range(i+1, n):
            complement = target - nums[j]

            if complement in complements:
                answers.add(tuple(sorted([nums[i], nums[j], complement])))
            else:
                complements.add(nums[j])

    return answers

nums = [0,0,0,0,0,0,0,0]
res = threeSum(nums)
print(res)

