def findTheDifference(s, t):
    s_sum = 0
    t_sum = 0
    for c in s:
        s_sum += ord(c)

    for c in t:
        t_sum += ord(c)

    return chr(t_sum - s_sum)

s = "abcd"
t = "abcde"
ans = findTheDifference(s, t)
print(ans)

