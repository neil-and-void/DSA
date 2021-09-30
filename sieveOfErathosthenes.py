import math

def getPrimes(n):
    if n < 2:
        return 0

    primes = [True for i in range(n)]
    primes[0] = False
    primes[1] = False

    # O(n**0.5)
    for p in range(2, math.floor((n)**0.5)+1):
        if primes[p] == True:
            mult = p

            # O(Log(Log(n)))
            while p * mult < n:
                primes[p * mult] = False
                mult += 1

    return len([p for p in range(n) if primes[p]])

n = 10
ans = getPrimes(n)
print(ans)
