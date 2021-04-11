'''
def intersection(nums1, nums2):
    put the smaller array into hash table where key is number and value is count

    intersected = []
    iterate over the other array
        check if num is in hash table
        if exists:
            add num to intersected
            decrement count of the value of the key
        else if not exists:
            do nothing

    time: o(n + m)
    space: o(2 * m)

    if sorted:

    intersected
    iterate over the other array
        find num in other array
        if exists:
            add num to intersected
            decrement count of the value of the key
        else if not exists:
            do nothing

    time: o(m * logn)
    space: o(m)
'''

def intersection(nums1, nums2):
    smaller = nums2
    bigger = nums1
    if len(nums1) < len(nums2):
        smaller = nums1
        bigger = nums2

    numCount = {}
    for num in smaller:
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1

    intersected = []
    for num in bigger:
        if num in numCount and numCount[num] > 0:
            intersected.append(num)
            numCount[num] -= 1
    return intersected

result = intersection([2,2,5,1,4,6,2,5,23,4,3,44,2],[2,45,2,1,5,6,3,4,3,12,24])
print(result)

