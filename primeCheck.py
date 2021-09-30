import math
def checkPrime(n):
    if n == 0 or n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for d in range(2, math.floor(n ** 0.5) + 1):
        if n % d == 0:
            return False

    return True

def countPrimes(n):
    count = 0
    for num in range(n):
        if checkPrime(num):
            count += 1
    return count

ans = countPrimes(2341)
print(ans)

