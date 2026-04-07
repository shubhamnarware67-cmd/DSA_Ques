"""
Q25: 0/1 Knapsack Problem (DP)
===============================
Problem: Given weights and values of n items, put items into a knapsack
of capacity W to get maximum total value.
Each item can only be taken once (0/1).

Example:
    values = [60, 100, 120], weights = [10, 20, 30], W = 50
    Output: 220  (items 2 and 3)
"""

def knapsack(W, weights, values, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    return dp[n][W]

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    print(knapsack(W, weights, values, len(values)))  # 220
