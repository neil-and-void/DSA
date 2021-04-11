def validPalindrome(s):
    # base case
    if len(s) <= 2:
        if len(s) <= 1:
            return True

        if len(s) == 2 and s[0] == s[1]:
            return True
        return False

    # recursive case
    if len(s) > 2:
        firstChar = s[0]
        lastChar = s[-1]

        return firstChar == lastChar and validPalindrome(s[1:-1])

print(validPalindrome('abba'))

