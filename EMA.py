"""

"""
def exponentialMovingAverage(prices, EMA_len):
    n = len(prices)
    i = 0
    SMOOTHING_FACTOR = 2 / (1 + EMA_len)

    prevEMA = 0
    EMA = 0

    # generate intial EMA
    for i in range(EMA_len):
        EMA += (prevEMA * (1 - SMOOTHING_FACTOR)) + (prices[i] * SMOOTHING_FACTOR)
        prevEMA = EMA

    i += 1
    while i < n:
        # remove left most EMA
        EMA -= (prices[i - EMA_len] * (SMOOTHING_FACTOR))

        EMA = (EMA * (1 - SMOOTHING_FACTOR)) + (prices[i] * SMOOTHING_FACTOR)

        print(EMA)

        i += 1

prices = [3,9,6,4,1222,6,3,1]
EMA_len = 4
ans = exponentialMovingAverage(prices, 4)
print(ans)
