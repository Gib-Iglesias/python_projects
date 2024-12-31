# -*- coding: utf-8 -*-


def maxProfit(prices, n):
    buy = prices[0]
    max_profit = 0
    for i in range(1, n):
        if (buy > prices[i]):
            buy = prices[i]
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit


if __name__ == '__main__':
    # Running the script, command line in terminal:
    # python3 buy_and_sell.py

    # Example Input: 71564
    # Example Output: 5
    prices = list(input('Ingresa una lista de números: '))
    prices = list(map(int, prices))
    n = len(prices)
    max_profit = maxProfit(prices, n)
    print('Max Profit: ',max_profit)
