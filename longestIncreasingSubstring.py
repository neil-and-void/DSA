from typing import *

def lengthOfLIS(arr: List[int]):
    for i in range(len(arr)):
        count = LIS_Rec(arr, float('-inf'), i, 1)
        print(count)

def LIS_Rec(arr, prev, cur_idx, length):
    if prev < arr[cur_idx]:
        max_count = 1
        for i in range(cur_idx):
            prev = arr[i]
            count = LIS_Rec(arr, prev, i+1, length+1)
            max_count = max(max_count, count)
    else:
        return length

arr = [10,9,2,5,3,7,101,18]
ans = lengthOfLIS(arr)
print(ans)

