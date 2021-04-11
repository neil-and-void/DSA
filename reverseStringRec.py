def reverseStringRec(string):
    # base case
    if len(string) <= 1:
        return string

    # recursive case
    lastChar = string[-1]
    return lastChar + reverseStringRec(string[:-1])

s = 'abcdefghi'
print(reverseStringRec(s))

