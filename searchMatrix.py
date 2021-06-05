'''
idea: binary search outter matrix
    * binary search innter matrix
def searchMatrix(matrix, target):
    m = row count
    n = col count

    lo = 0
    hi = m - 1
    
    while lo <= hi
        mid = lo + ((hi - lo) // 2)

        if target in range of matrix[mid]
            found the array, break

        if less than the first element of matrix
            hi = mid - 1 

        if greater then the first element of matrix
            lo = mid - 1

    binary search the array
'''
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    lo = 0
    hi = m - 1
    arr = None

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        if matrix[mid][0] <= target and target <= matrix[mid][-1]:
            arr = matrix[mid]
            break

        elif target < matrix[mid][0]:
            hi = mid - 1

        elif matrix[mid][-1] < target:
            lo = mid + 1

    if arr == None:
        return False

    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1

    return False

m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
ans = searchMatrix(m, target)
print(ans)

