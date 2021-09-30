from typing import *

def peakIndexInMountainArray(arr: List[int]) -> int:
    n = len(arr)
    lo = 0
    hi = n - 1

    while lo <= hi:
        m = lo + ((hi - lo) // 2)

        if m > 0 and m < n - 1 and arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
            return m

        if arr[m] < arr[m+1]:
            lo = m + 1

        elif arr[m] > arr[m+1]:
            hi = m - 1

arr = [24,69,100,99,79,78,67,36,26,19]
ans = peakIndexInMountainArray(arr)
print(ans)

