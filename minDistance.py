'''
notes:
* when a problem is really REALLY hard to find a pattern in due to complexity,
    break up it into very VERY VERY tiny pieces
* when breaking a problem up, might have to go really tiny pieces

def minDistance(word1, word2):
    # base
    if len(word1) == 1 and len(word2) == 1:
        if word1 == word2:
            return 0
        else:
            return 1
    elif len(word1) == 0:
        return len(word2)
    elif len(word2) == 0:
        return len(word1)

    # recursive
    else:
        insert = minDistance(word1[:-1], word2) + 1
        delete = minDistance(word1, word2[:-1]) + 1
        replace = minDistance(word1[:-1], word2[:-1])
        if word1[-1] != word2[-1]:
            replace += 1
        return min(insert, min(delete, replace))
'''

# dynamic programming bottom up, use base and recursive case from previous to turn into base and iterative case, respectively, for buttom up
def minDistance(word1, word2):
    if word1 == word2:
        return 0

    n = len(word1)
    m = len(word2)

    minEditDistancesAt = [[float('inf') for i in range(n + 1)] for j in range(m+1)]

    # base cases
    for j in range(m+1):
        minEditDistancesAt[j][0] = j
    for i in range(n+1):
        minEditDistancesAt[0][i] = i

    # iterative cases
    for w2_len in range(1, m+1):
        for w1_len in range(1, n+1):
            delete = minEditDistancesAt[w2_len - 1][w1_len]+ 1
            insert = minEditDistancesAt[w2_len][w1_len - 1] + 1
            replace = minEditDistancesAt[w2_len - 1][w1_len - 1]
            if word1[w1_len - 1] != word2[w2_len - 1]:
                replace += 1
            minEditDistancesAt[w2_len][w1_len] = min(delete, min(insert, replace))

    return minEditDistancesAt[-1][-1]

word1 = "a"
word2 = ""
ans = minDistance(word1, word2)
print(ans)

