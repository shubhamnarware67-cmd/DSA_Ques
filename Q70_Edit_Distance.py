"""
Q70: Edit Distance (Levenshtein Distance) - DP
===============================================
Problem: Given two strings word1 and word2, return the minimum number of
operations (insert, delete, replace) required to convert word1 to word2.

Example:
    "horse" -> "ros" = 3 operations
    "intention" -> "execution" = 5 operations
"""

def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

if __name__ == "__main__":
    print(min_distance("horse", "ros"))        # 3
    print(min_distance("intention","execution"))# 5
