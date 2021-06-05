'''
observations:
- at any given cell, all items above are smaller (same for items to the left)
- at any given cell, all items below are biggert (same for items to the right)

idea: binary search for which rows the target could be in by range,
        search rows, O(m logn)

idea: search by row, then by column
- if in column i, can't it be in column i - j?

idea:
'''
from typing import *

# brute force binary search
'''
def searchMatrixII(matrix: List[List[int]], target: int) -> bool:
    for arr in matrix:
        if arr[0] <= target and target <= arr[-1]:
            lo = 0
            hi = len(arr) - 1

            while lo <= hi:
                mid = lo + ((hi - lo) // 2)

                if arr[mid] == target:
                    return True

                elif target < arr[mid]:
                    hi = mid - 1

                elif arr[mid] < target:
                    lo = mid + 1
    return False
'''
##############################################################################
'''
idea: each cell is about the middle of a L shaped array, kinda like a binary earch
'''
def searchMatrixII(matrix, target):
    pass

m = [[1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]]
target = 11
ans = searchMatrix(m, target)
print(ans)

