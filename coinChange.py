'''
cache = dict()

# recursive with caching
def coinChange(coins, amount):
    if amount in cache:
        return the value to that key

    # base case
    if the amount is 0
        return 0

    if the amount is equal to one of the coins
        return 1

    if the amount is less than smallest coin
        return -1

    # recursive
    min of (coinChange(coins, amount - c_0),...coinChange(coins, amount - c_n)) + 1
    put min of the above in cache
    return that value
'''
from typing import *

### brute recursion ###
# def coinChangeRec(coins: List[int], amount: int, coinChangeCache) -> int:
#    if amount in coinChangeCache:
#        return coinChangeCache[amount]
#
#    # base case
#    if amount == 0:
#        return 0
#
#    if amount in coins:
#        return 1
#
#    if amount < min(coins):
#        return -1
#
#    # recursive case
#    quantities = []
#    for coin in coins:
#        quantities.append(coinChangeRec(coins, amount - coin, coinChangeCache) + 1)
#
#    allZeroes = True
#    for quantity in quantities:
#        if quantity != 0:
#            allZeroes = False
#
#    if allZeroes:
#        return -1
#
#    noneZeroMin = float('inf')
#    for quantity in quantities:
#        if quantity != 0:
#            noneZeroMin = min(noneZeroMin, quantity)
#
#    if amount not in coinChangeCache:
#        coinChangeCache[amount] = noneZeroMin
#
#    return noneZeroMin
#
#def coinChange(coins, amount):
#    coinChangeCache = {}
#    return coinChangeRec(coins, amount, coinChangeCache)
### brute recursion ###

'''
# iterative using recursive defintion bottom up
def coinChange(coins, amount):
    # base cases #
    if amount equals 0
        return 0

    smallestCoin = min(coins)

    if amount < smallestCoin
        return -1

    minCoinQuantities = build an array of zeros size amount + 1

    for each coin, use coin as index to value 1

    # base cases end #

    for i from 0 to amount + 1
        minQuantity = inf
        for each coin, if i - coin is >= 0 and cached[i - coin] is not -1
            minQuanity = min of minQuantity and cached[i - coin]
        minQuantity[i] = minQuantity

    return minQuantity[amount]
'''
def coinChangeOPTION_ONE(coins, amount):
    # base cases #
    if amount == 0:
        return 0

    smallestCoin = min(coins)

    if amount < smallestCoin:
        return -1
    minCoinQuantities = [0 for i in range(amount + 1)]
    # base cases end #

    # iterative using recursive cases
    for i in range(1, amount + 1):
        quantities = []
        for coin in coins:
            if i - coin >= 0 and minCoinQuantities[i - coin] != -1:
                quantities.append(minCoinQuantities[i - coin] + 1)

        if len(quantities) == 0:
            minCoinQuantities[i] = -1
        else:
            minCoinQuantities[i] = min(quantities)
    return minCoinQuantities[amount]

'''
very slight optimization of the above solution,
    instead of setting the default values of the array to 0
    set them to infinity and check if possible to make amount at the
    last step. And for each step, if we find that we aren't able
    to find a value lower than inf, that there was no value being able to find
'''
def coinChange(coins: List[int], amount: int) -> int:
    # base cases #
    if amount == 0:
        return 0

    smallestCoin = min(coins)

    if amount < smallestCoin:
        return -1
    minCoinQuantities = [float('inf') for i in range(amount + 1)]

    minCoinQuantities[0] = 0
    # base cases end #

    # iterative using recursive cases
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and minCoinQuantities[i - coin] != -1:
                minCoinQuantities[i] = min(minCoinQuantities[i - coin] + 1, minCoinQuantities[i])

    if minCoinQuantities[amount] == float('inf'):
        return -1
    return minCoinQuantities[amount]

coins = [2]
amount = 11
res = coinChange(coins, amount)
print(res)

