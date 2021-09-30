def lengthOfLIS(arr):
    prev = float('-inf')
    m_count = 1
    memo = dict()
    for i in range(len(arr)):
        m_count = max( lengthOfLIS_rec(arr, prev, i, memo), m_count)
    return m_count

def lengthOfLIS_rec(arr, prev, i, memo):
    if i in memo and prev < arr[i]:
        return memo[i]
    # base
    if i == len(arr) - 1 and prev < arr[i]:
        return 1
    if prev >= arr[i]:
        return 0

    # recursive
    else:
        prev = arr[i]
        longest = 1
        for j in range(i+1, len(arr)):
            longest = max(lengthOfLIS_rec(arr, prev, j, memo) + 1, longest)
        memo[i] = longest
        return longest

arr = [10,9,2,5,3,7,101,18]
ans = lengthOfLIS(arr)
print(ans)

