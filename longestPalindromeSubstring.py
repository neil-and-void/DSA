def longestPalindrome(s):
    n = len(s)
    if n == 0:
        return ''

    longest_palindrome_indices = [0,0]
    for i in range(n-1):
        l = i
        r = i

        while 0 <= l - 1 and r + 1 < n and s[l - 1] == s[r + 1]:
            l -= 1
            r += 1

        if longest_palindrome_indices[1] - longest_palindrome_indices[0] < r - l:
            longest_palindrome_indices = [l, r]

        if s[i] == s[i+1]:
            l = i
            r = i + 1

            while 0 <= l - 1 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            if longest_palindrome_indices[1] - longest_palindrome_indices[0] < r - l:
                longest_palindrome_indices = [l, r]

    return s[longest_palindrome_indices[0]: longest_palindrome_indices[1]+1]

# s = "cbabd"
# ans = longestPalindrome(s)
# print(ans)

def manachersAlg(s):
    n = len(s)
    '''
    string = []
    for c in s:
        string.append('#')
        string.append(c)
    string.append('#')
    '''
    for i in range(n):
        print(i)

s = 'cababsc'
ans = manachersAlg(s)
print(ans)

