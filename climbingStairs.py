'''
def climbStairs(n):
    # base
    n == 1 => 1
    n == 2 => 2


    #recursive n > 2
    return (climbStairs(n - 1) + 1) + (climbStairs(n - 2) + 2)

idea cache results seen before
def climbStairs(n):
    blah blah blah

idea: start from base and build up to n
def climbStairs(n):
    uniqueClimbs = create array of 0's of length n + 1

    # base cases
    uniqueClimbs[1] = 1
    uniqueClimbs[2] = 2

    # iterative (recursive-ish)
    for i from 3 to n + 1
        uniqueClimbs[i] = uniqueClimbs[i-1] + uniqueClimbs[i-2]
    return uniqueClimbs[n]


'''

def climbStairs(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if 2 < n:
        return(climbStairs(n - 1)) + (climbStairs(n - 2))

def climbStairs(n):
    uniqueClimbs = [0 for i in range(n+1)]

    uniqueClimbs[1] = 1
    uniqueClimbs[2] = 2

    for i in range(3,n + 1):
        uniqueClimbs[i] = uniqueClimbs[i-1] + uniqueClimbs[i-2]
    return uniqueClimbs[n]

n = 18
res = climbStairs(n)
print(res)
