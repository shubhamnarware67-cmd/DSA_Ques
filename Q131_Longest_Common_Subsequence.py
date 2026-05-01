"""
Q131: Longest Common Subsequence (LCS) - DP
=============================================
Problem: Given two strings, return the length of their longest common
subsequence (not necessarily contiguous).

Example:
    "abcde", "ace" -> 3  ("ace")
    "abc", "abc"   -> 3
    "abc", "def"   -> 0
"""

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))  # 3
    print(longest_common_subsequence("abc", "abc"))    # 3
    print(longest_common_subsequence("abc", "def"))    # 0
