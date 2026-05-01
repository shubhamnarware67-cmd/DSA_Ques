"""
Q132: Distinct Subsequences (DP)
==================================
Problem: Given strings s and t, return number of distinct subsequences
of s which equals t.

Example:
    s="rabbbit", t="rabbit" -> 3
    s="babgbag", t="bag"    -> 5
"""

def num_distinct(s, t):
    m, n = len(s), len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]
    return dp[m][n]

if __name__ == "__main__":
    print(num_distinct("rabbbit", "rabbit"))  # 3
    print(num_distinct("babgbag", "bag"))     # 5
