"""
Q189: Longest Common Subsequence of Three Strings (3D DP)
===========================================================
Problem: Find LCS of three strings.

Example:
    s1="geeks", s2="geeksfor", s3="geeksforgeeks" -> 5 ("geeks")
    s1="abcd1e2", s2="bc12ea", s3="bd1ea" -> 3 ("b1e" or "bde")
"""

def lcs_three(s1, s2, s3):
    l, m, n = len(s1), len(s2), len(s3)
    dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(l+1)]
    for i in range(1, l+1):
        for j in range(1, m+1):
            for k in range(1, n+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[l][m][n]

if __name__ == "__main__":
    print(lcs_three("geeks","geeksfor","geeksforgeeks"))  # 5
    print(lcs_three("abcd1e2","bc12ea","bd1ea"))          # 3
