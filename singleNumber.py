'''
idea 0: check if number in a set, if it is, then subtract it, else, add to set

idea 1: use bitwise xor to allow pairs to cancel themselves out
'''
from typing import *
def singleNumber(nums: List[int]) -> int:
    n = 0
    for i in range(len(nums)):
        n ^= nums[i]
    return n

nums = [5,1,2,1,2,7,7,4,4]
ans = singleNumber(nums)
print(ans)

