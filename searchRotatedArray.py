'''
idea: find pivot, then use that alongside regular binary search
def search(nums: List[int], target: int) -> int:
    # find true beginning of array
    pivot = last element of array

    lo = 0

    while lo <= pivot
        mid = calc mid

        if mid less than pivot
            pivot = mid - 1

        if mid greater than pivot
            lo = mid + 1

    pivot is at correct spot
    determine wheterh we wan to search lower or upper partition by comparing against the last element
    if bigger than last
        serach between 0 and pivot - 1
    if smaller
        search between pivot and n - 1
'''
from typing import *
def search(nums: List[int], target: int) -> int:
    n = len(nums)

    if n == 1:
        if nums[0] == target:
            return 0
        return -1

    pivot = n - 1
    lo = 0

    while lo <= pivot:
        mid = lo + ((pivot - lo) // 2)
        if nums[mid-1] > nums[mid]:
            print('hi')
            break

        if nums[mid] < nums[pivot]:
            pivot = mid - 1

        elif nums[pivot] < nums[mid]:
            lo = mid + 1

    if target == nums[-1]:
        return n - 1

    if target > nums[-1]:
        # search upper partition
        lo = 0
        hi = mid - 1
    elif target < nums[-1]:
        # search lower partition
        lo = mid
        hi = n - 1

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            hi = mid - 1

        if nums[mid] < target:
            lo = mid + 1
    return -1


nums = [3,1]
target = 0
ans = search(nums, target)
print(ans)

