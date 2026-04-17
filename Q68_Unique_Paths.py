"""
Q68: Unique Paths (DP)
======================
Problem: A robot is on m x n grid, starts at top-left, wants to reach
bottom-right. It can only move right or down. Count unique paths.

Example:
    m=3, n=7 -> 28
    m=3, n=2 -> 3
"""

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]

# Math (Combinatorics): C(m+n-2, n-1)
from math import comb
def unique_paths_math(m, n):
    return comb(m + n - 2, n - 1)

if __name__ == "__main__":
    print(unique_paths(3, 7))       # 28
    print(unique_paths_math(3, 2))  # 3
