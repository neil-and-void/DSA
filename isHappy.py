from typing import *

def isHappy(n: int) -> bool:
    slow = getNext(n)
    fast = getNext(getNext(n))

    while slow != 1 and fast != 1:
        slow = getNext(slow)
        fast = getNext(getNext(fast))

        if slow == fast:
            return False
    return True

def getNext(n):
    next = 0
    while n != 0:
        digit = n % 10
        next += digit ** 2
        n //= 10
    return next

n = 12
ans = isHappy(n)
print(ans)

