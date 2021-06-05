'''
idea: use heap for count of each letter and append the letters with the most count to both sides
def reorganizeString(S):
    charCount = map
    for each character in S
        if character not in charCount
            add it to charcount
        else, it is
            increment count
    for each kvPair in charCount
        add to heap

    while heap is not empty
        pop top element
        if popped element is the same as the one of the elements on the end
            if heap is empty
                return empty string
            else
                append to ends and continue on
        put the char of that element on both sides of the string
        if it has leftover still
            add it back to the heap

    return string

import heapq

def reorganizeString(S):
    charCount = {}
    for character in S:
        if character not in charCount:
            charCount[character] = 1
        else:
            charCount[character] += 1
    maxHeap = []


    for c in charCount:
        heapq.heappush(maxHeap, (-charCount[c], c))

    pair = heapq.heappop(maxHeap)
    count = -pair[0]
    c = pair[1]
    heapq.heappush(maxHeap, (-1 * (count - 1), c))
    ans = c

    while len(maxHeap) > 0:
        pair = heapq.heappop(maxHeap)
        count = pair[0] * -1
        c = pair[1]

        # TODO: need to check if characters of pop are the same on the ends, if so, pop again
        if c == ans[-1] or c == ans[0]:
            if len(maxHeap) == 0:
                return ''
            diffPair = heapq.heappop(maxHeap)
            diffCount = -diffPair[0]
            diffChar = diffPair[1]
            if diffCount == 1:
                ans += diffChar
                diffCount = 0
            elif diffCount > 1:
                ans = diffChar + ans + diffChar
                diffCount -= 2
            if diffCount > 0:
                heapq.heappop(maxHeap, (-diffCount, diffChar))

        if count == 1:
            ans += c
            count = 0
        elif count > 1:
            ans = c + ans + c
            count -= 2

        if count > 0:
            heapq.heappush(maxHeap, (-1 * count, pair[1]))

    return ans
'''

'''
idea: try to exhaust the most frequent letters
def reorganizeString(S):
    create maxheap of character frequency

    start ans with 1 character of the most frequent

    while the heap is not empty:
        mostFrequent = maxheap pop the top

        if the mostfrequent char is different from both sides of string
            if mostFrequentChar is greater than 1
                add character to both sides
            else if it is only 1
                add character to one side
        if most freq char is same as one of the sides
            try popping again for second frequent char
                if heap is empty
                    stop and return
                # else add it
                if secondFreq is greater than 1
                    add character to both sides
                else if it is only 1
                    add character to the side that is same as mostFrequent
'''
'''
def reorganizeString(S):
    import heapq
    from collections import defaultdict

    charCount = defaultdict(lambda: 0)
    for c in S:
        charCount[c] += 1

    maxHeap = []
    for key in charCount:
        heapq.heappush(maxHeap, (-charCount[key], key))

    mostFreq = heapq.heappop(maxHeap)
    ans = mostFreq[1]
    heapq.heappush(maxHeap, ((mostFreq[0] ) + 1, mostFreq[1]))


    while len(maxHeap) > 0:
        mostFreq = heapq.heappop(maxHeap)
        mFCount = -mostFreq[0]
        mFChar = mostFreq[1]

        if mFChar == ans[0] and mFChar == ans[-1]:
            if len(maxHeap) == 0:
                return ''
            secondFreq = heapq.heappop(maxHeap)
            sFCount = -secondFreq[0]
            sFChar = secondFreq[1]

            if sFCount > 1:
                ans = sFChar + ans + sFChar
                sFCount -= 2
            else:
                if ans[-1] == mFChar:
                    ans = sFChar + ans
                else:
                    ans = ans + sFChar
                sFCount -= 1
            if sFCount > 0:
                heapq.heappush(maxHeap, (-sFCount, sFChar))

        else:
            if mFCount > 1:
                ans = mFChar + ans + mFChar
                mFCount -= 2
            else:
                ans = mFChar + ans
                mFCount -= 1


        if mFCount > 0:
            heapq.heappush(maxHeap, (-mFCount, mFChar))

    return ans
'''
'''
idea:
    - exhaust the most frequent character as much as possible in a valid way
    - define this valid way as a string 'XYXYXYXYXYXYXY' where for all X and Y, X != Y
    - we choose the most frequent as this will allow us 
def reorganizeString(S):
    create heap of charCounts and their chars

    ans = empty array
    while heap is not empty
        pop mostFreq

        if mostFreq is a the same as the last element
            if no more characters to pad the string to allow the mostfreq to be appended to
                return fail state ie. ''
            pop again and append second freq
        if mostFreq is not same as the last elemetn
            append to end
    ans => string
    return

'''
def reorganizeString(S):
    import heapq
    from collections import defaultdict
    if len(S) == 0:
        return ""

    charCount = defaultdict(lambda: 0)
    for c in S:
        charCount[c] += 1

    maxHeap = []
    for key in charCount:
        heapq.heappush(maxHeap, (-charCount[key], key))

    mostFreq = heapq.heappop(maxHeap)

    mostFreqCount = -mostFreq[0]
    mostFreqChar = mostFreq[1]
    ans = [mostFreqChar]
    mostFreqCount -= 1
    if mostFreqCount > 0:
        heapq.heappush(maxHeap, (-mostFreqCount, mostFreqChar))

    print(maxHeap)
    while len(maxHeap) > 0:
        mostFreq = heapq.heappop(maxHeap)
        mostFreqCount = -mostFreq[0]
        mostFreqChar = mostFreq[1]

        if mostFreqChar == ans[-1]:
            if len(maxHeap) == 0:
                return ''
            secFreq = heapq.heappop(maxHeap)
            secFreqCount = -secFreq[0]
            secFreqChar = secFreq[1]

            ans.append(secFreqChar)
            secFreqCount -= 1

            if secFreqCount > 0:
                heapq.heappush(maxHeap, (-secFreqCount, secFreqChar))

        ans.append(mostFreqChar)
        mostFreqCount -= 1

        if mostFreqCount > 0:
            heapq.heappush(maxHeap, (-mostFreqCount, mostFreqChar))

    return ''.join(ans)


S = ""
ans  = reorganizeString(S)
print(ans)

