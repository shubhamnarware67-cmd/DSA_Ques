"""
Q23: Coin Change (DP)
=====================
Problem: Given coins of different denominations and a total amount,
find the minimum number of coins to make up that amount.
Return -1 if it's not possible.

Example:
    coins = [1, 5, 6, 9], amount = 11
    Output: 2  (5+6)
"""

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print(coin_change([1, 5, 6, 9], 11))  # 2
    print(coin_change([1, 2, 5], 11))     # 3
    print(coin_change([2], 3))            # -1
