'''
idea: go k mod n index, copy to new array until second half copied, then copy first half up to but not including same index
- uses n space 
def rotate(nums, k):
    pass


idea: copy k last elenents into a temp arr, rotate by k with by copy numbers to another pointer, copy k into the k first spots
def rotate(nums, k):
'''
def rotate(nums, k):
    n = len(nums)
    secondSlice = nums[-k:n]
    print(nums)

    # rotate first half
    firstHalfLen = n - (k % n)
    for i in range(firstHalfLen):
        print(i)
        nums[i+(k % n)] = nums[i]
      
    # apply second half to array
    i = 0
    for num in secondSlice:
        nums[i] = num
        i += 1

    return nums

nums = [1,2,3,4,5,6,7]
k = 3
ans = rotate(nums, k)
print(ans)

