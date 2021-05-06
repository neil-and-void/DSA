def binarySearch(arr, target):
    '''
    get middle element
    if middle element is target
        return index
    if target is greater than middle
        search right
    if target is less than middle
        search right
    if serach boundaries cross
        return -1
    '''
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        if arr[mid] == target:
            return mid

        if target < arr[mid]:
            hi = mid - 1

        if arr[mid] < target:
            lo = mid + 1
    return -1

arr = [1,3,4,5,6,8,12,14,15,18,20,21]

target = 15
ans = binarySearch(arr, target)
print(ans)
print(arr[ans] == target)

