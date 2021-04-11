'''

def maxProfit(prices):
    base = 0
    price = 1
    profit = 0

    for price from 0 to n - 1
        price - base
        if negative, price is new base
        if positive, profit = max(price - base, profit)
'''
def maxProfit(prices):
    if len(prices) == 1:
        return 0

    base = prices[0]
    profit = 0

    for i in range(len(prices)):
        currentProfit = prices[i] - base

        if currentProfit < 0:
            base = prices[i]

        if currentProfit > 0:
            profit = max(profit, currentProfit)

    return profit

prices = [7,6,4,3,1]
res = maxProfit(prices)
print(res)

