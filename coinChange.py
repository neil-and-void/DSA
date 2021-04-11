from typing import List
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


# iterative using recursive defintion bottom up
def coinChange(coins, amount):

'''


def coinChange(coins: List[int], amount: int) -> int:



coins = [2]
amount = 3
res = coinChange(coins, amount)
print(res)

