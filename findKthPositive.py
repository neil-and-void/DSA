'''
#idea: iterate through arr and add missing numbers to a new array until size reaches k
def findKthPositive(arr, k):

    n = len(arr)
    currentMissing = 1
    missing = []

    for each item in the array
        if currentMissing is < item
            add all currentMissings (ie. all currentMissing < item) to a new array
        currentMissing += 1

    return missing[k-1]
'''


def findKthPositive(arr, k):
    n = len(arr)
    currentMissing = 1
    missing = []

    for number in arr:
        print(currentMissing, number, missing)
        while currentMissing < number:
            missing.append(currentMissing)
            currentMissing += 1
        currentMissing+= 1

    # if length of missing arr = 0
    if len(missing) == 0:
        currentMissing += 1
        missing.append(currentMissing)

    # if length of missing arr < k
    while len(missing) < k:
        missing.append(currentMissing)
        currentMissing += 1
    return missing[k - 1]


arr = [5,6,7,8,9]
k = 9
res = findKthPositive(arr, k)
print(res)

