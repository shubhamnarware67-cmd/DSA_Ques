"""
Q59: Best Time to Buy and Sell Stock
=====================================
Problem: Given prices array, find the maximum profit by buying on
one day and selling on a later day. Return 0 if no profit possible.

Example:
    [7,1,5,3,6,4] -> 5  (buy at 1, sell at 6)
    [7,6,4,3,1]   -> 0
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # 5
    print(max_profit([7,6,4,3,1]))    # 0
