'''
idea: backtracking
pseudo code
def permuteRec(nums, candidateList, candidateSet, ansList):
    # base
    if candidateSet same size as nums
        add candidate list to ansList
        return

    # recursive case
    for each num in nums
        if num not in candidate set
            append to end of candidate list
            add to candidate set
            recurse()
            pop from candidate set
            pop from end of list
'''
def permute(nums):
    from copy import deepcopy
    def permuteRec(nums, candidateList, candidateSet, ansList):
        if len(candidateList) == len(nums):
            newAns = deepcopy(candidateList)
            ansList.append(newAns)
            return
        else:
            for num in nums:
                if num not in candidateSet:
                    candidateList.append(num)
                    candidateSet.add(num)
                    permuteRec(nums, candidateList, candidateSet, ansList)
                    candidateList.pop()
                    candidateSet.remove(num)
    ansList = []
    candidateSet = set()
    candidateList = []
    permuteRec(nums, candidateList, candidateSet, ansList)
    return ansList

nums = [1,2,3]
ans = permute(nums)
print(ans)

