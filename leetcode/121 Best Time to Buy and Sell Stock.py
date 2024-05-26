stonks = [7, 1, 5, 3, 6, 4]
stonks_2 = [7, 6, 4, 3, 1]


def maxProfit(prices):

    minim = prices[0]
    delta = 0

    for val in prices[1:]:
        if (val - minim > delta):
            delta = val - minim

        if val < minim:
            minim = val

    return delta


print(f'profit = {maxProfit(stonks)}')
print(f'profit_2 = {maxProfit(stonks_2)}')
