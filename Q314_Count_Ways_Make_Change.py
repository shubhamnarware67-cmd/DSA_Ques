"""
Q314: Coin Change 2 — Count Ways (Unbounded Knapsack)
======================================================
Problem: Count number of combinations of coins that make up the amount.

Example:
    amount=5, coins=[1,2,5] -> 4
    (5=5, 5=2+2+1, 5=2+1+1+1, 5=1+1+1+1+1)
    amount=3, coins=[2]     -> 0
"""

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]

if __name__ == "__main__":
    print(change(5, [1,2,5]))   # 4
    print(change(3, [2]))        # 0
    print(change(10, [10]))      # 1
    print(change(500, [1,2,5]))  # 12701
