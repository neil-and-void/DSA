'''
idea: backtracking (no shit)
def splitString():

def splitStringRec(s, prev, candidate, searchEdge):
    # base
    if prev - candidate != 1
        return false

    # recursive
    else if prev - candidate == 1
        for i from searchedge to end of string
            append number at i to end of candidate
            valid = splitStringRec()
            if valid:
                return true
        return false
'''
def splitString(s):
    for i in range(0, len(s)):
        candidate = 
        valid = splitStringRec(s, i+1, )
        if valid:
            return true

def splitStringRec(s, searchLimit, prev, candidate):
    # base case
    if prev - candidate != 1:
        return False

    elif prev - candidate == 1:
        cur = candidate
        for i in range(searchLimit, len(s)):
            cur *= 10
            cur += int(s[i])
            valid = splitStringRec(s, i+1, candidate, cur)
            if valid:
                return true
        return false

s = '050043'
ans = splitString(s)
print(ans)

