def search(target, array, lo):
    hi = len(array) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if array[mid] == target:
            return mid

        if target < array[mid]:
            hi = mid - 1

        elif array[mid] < target:
            lo = mid + 1
    return -1

def twoSum(numbers, target):
    for i in range(len(numbers)):
        complement = target - numbers[i]
        complementIndex = search(complement, numbers, i + 1)

        if complementIndex != -1:
            return [i + 1, complementIndex + 1]

def main():
    a = [-1, 0]
    t = -1
    result = twoSum(a, t)
    print(result)


if __name__ == '__main__':
    main()

