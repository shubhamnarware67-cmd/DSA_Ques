"""
Q278: Guess Number Higher or Lower II (Minimax DP)
====================================================
Problem: Guessing game from 1 to n. Worst-case minimum money to guarantee win.
If wrong: pay that number, target is higher or lower.

Example:
    n=10 -> 16
    n=1  -> 0
    n=2  -> 1
"""

def get_money_amount(n):
    dp = [[0]*(n+2) for _ in range(n+2)]
    for length in range(2, n+1):
        for start in range(1, n-length+2):
            end = start + length - 1
            dp[start][end] = float('inf')
            for k in range(start, end+1):
                cost = k + max(dp[start][k-1], dp[k+1][end])
                dp[start][end] = min(dp[start][end], cost)
    return dp[1][n]

if __name__ == "__main__":
    print(get_money_amount(10))  # 16
    print(get_money_amount(1))   # 0
    print(get_money_amount(2))   # 1
