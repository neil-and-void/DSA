def firstUniqChar(s):
    charCount = dict()
    for c in s:
        if c in charCount:
            charCount[c] += 1
        else:
            charCount[c] = 1
    for i in range(len(s)):
        if charCount[s[i]] == 1:
            return i

    return -1
