'''
idea: modified binary search
def searchRange(nums, target):

    // upper //
    // failure base case
    if hi <= lo
        failed and return [-1, -1]

    mid = calculate mid

    // success base case
    if mid element equal to target and the next element is diff or out of list
        found the upper range

    // recursive cases
    if mid element greater than our target
        search(lo, mid)

    if mid element and next to mid element is target or mid element is less than the target
        search(mid, hi)

    // lower
    if <= lo
        failed and return

    mid = calculate mid

    // success case
    mid element equals target and left of mid is different or out of the range (ie, not equal)
        return [mid, upper]

    // recursive cases
    if mid element is smaller than our target
        search(mid, hi)

    if mid element is greater than our target or mid element and mid -1 element are equal to target
        search(lo, mid)


'''


def searchRange(nums, target):
    lo = 0
    hi = len(nums) - 1
    upper = -1
    lower = -1

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        # success
        if nums[mid] == target and (((mid + 1 < len(nums)) and nums[mid+1] != nums[mid]) or (mid + 1 >= len(nums))):
            upper = mid
            break

        elif target < nums[mid]:
            hi = mid - 1

        elif nums[mid] <= target:
            lo = mid + 1

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        # success
        print(mid)
        if nums[mid] == target and ((mid - 1 >= 0 and nums[mid-1] != nums[mid]) or (mid - 1 < 0)):
            print('hi')
            lower = mid
            break

        elif nums[mid] < target:
            lo = mid + 1

        elif target <= nums[mid]:
            hi = mid - 1

    return [lower, upper]


'''
idea: modified binary search
def searchRange(nums, 8):
    lo = 0
    hi = n - 1
    # uppper
    while hi is above or equal to lo
        mid = calculate mid
        # found upper
        if mid is target and mid + 1 is not target or is end of array
            return mid

        # above upper
        if target < mid
            hi = mid - 1

        # below upper
        if mid <= target
            lo = mid + 1
    # lower
    lo = 0
    hi = n - 1

    while hi is above or equal to lo
        mid = calculaet mid

        if mid is equal to target and mid - 1 is eiter out of array or different from target
            return mid

        below left edge
        if mid < target
            lo = mid + 1

        above left edge
        if target <= mid
            hi = mid - 1

'''
# def searchRange(nums, target):
#     n = len(nums)
#     lo = 0
#     hi = n - 1
#     ans = [-1, -1]

#     while lo <= hi:
#         mid = lo + ((hi - lo)//2)

#         # 1
#         if nums[mid] == target and ((mid + 1 < n and nums[mid+1] != target) or (mid + 1 >= n)):
#             ans[1] = mid
#             break

#         # 2
#         if target < nums[mid]:
#             hi = mid - 1

#         # 3
#         if nums[mid] <= target:
#             lo = mid + 1

#     # lower
#     lo = 0
#     hi = n - 1

#     while lo <= hi:
#         mid = lo + ((hi - lo) // 2)

#         if nums[mid] == target and ((0 <= mid - 1 and nums[mid - 1] != target) or (mid - 1 < 0)):
#             ans[0] = mid
#             break

#         # 1
#         if nums[mid] < target:
#             lo = mid + 1

#         # 2
#         if target <= nums[mid]:
#             hi = mid - 1

#     return ans

nums = [1, 2, 3, 4, 5, 5, 5, 6, 8, 8, 10, 11, 11]
target = 8
ans = searchRange(nums, target)
print(ans)
