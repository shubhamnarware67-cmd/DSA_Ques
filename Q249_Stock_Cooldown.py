"""
Q249: Best Time to Buy and Sell Stock with Cooldown (DP)
=========================================================
Problem: After selling, you must wait one day (cooldown) before buying.
Find max profit.

Example:
    [1,2,3,0,2] -> 3  (buy@1,sell@2,buy@0,sell@2 with cooldown)
    [1]          -> 0
"""

def max_profit_cooldown(prices):
    if len(prices) <= 1: return 0
    n = len(prices)
    hold  = -prices[0]    # Holding a stock
    sold  = 0             # Just sold (cooldown next)
    rest  = 0             # Resting (can buy)
    for i in range(1, n):
        prev_hold, prev_sold, prev_rest = hold, sold, rest
        hold  = max(prev_hold, prev_rest - prices[i])  # Hold or buy
        sold  = prev_hold + prices[i]                   # Sell today
        rest  = max(prev_rest, prev_sold)               # Rest or stay rested
    return max(sold, rest)

if __name__ == "__main__":
    print(max_profit_cooldown([1,2,3,0,2]))  # 3
    print(max_profit_cooldown([1]))           # 0
    print(max_profit_cooldown([2,1,4]))       # 3
