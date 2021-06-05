'''
learned: difference between backtracking and brute force is that there is a **BASE CASE** that
         ends the recursion earlier than not
idea: iterate and dfs to the depth of k and backtrack if we are greater or equal to the sum
def combinationSum3(k, n):
    candidate = []
    ans = []
    combinationSum3Rec(k, n, 0, candidate, 0, ans)

def combinationSum3Rec(k, n, searchLimit, candidate, candidateSum, ans):
    # base
    if candidateSum is equal to n
        add candidate to answers

    if candidateSum is greater than n
        return

    # recursive
    for i from searchLimit to k-1
        add i to candidate
        add i to candidateSum
        combinationSum3Rec(k, n, searchLimit + 1, candidate, ans)
        undo the add to candidate and candidateSum
'''
import copy

def combinationSum3(k, n):
    candidate = []
    ans = []
    combinationSum3Rec(k,n,1,candidate,0,ans)
    return ans

def combinationSum3Rec(k, n, searchLimit, candidate, candidateSum, ans):
    # base
    if candidateSum > n or len(candidate) > k:
        return

    if candidateSum == n and len(candidate) == k:
        newAns = copy.deepcopy(candidate)
        ans.append(newAns)

    # recursive
    for i in range(searchLimit, 9+1):
        candidate.append(i)
        candidateSum += i
        combinationSum3Rec(k, n, i+1, candidate, candidateSum, ans)
        candidate.pop()
        candidateSum -= i

k = 4
n = 1
ans = combinationSum3(k, n)
print(ans)

