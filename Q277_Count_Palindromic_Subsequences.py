"""
Q277: Count Different Palindromic Subsequences (DP)
====================================================
Problem: Count distinct palindromic subsequences in string s. Return mod 10^9+7.
Only characters a,b,c,d.

Example:
    "bccb" -> 6  (b,c,bb,cc,bcb,bccb)
    "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba" -> 104860361
"""

def count_palindromic_subsequences(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                lo, hi = i+1, j-1
                while lo <= hi and s[lo] != s[i]: lo += 1
                while lo <= hi and s[hi] != s[j]: hi -= 1
                if lo > hi:
                    dp[i][j] = dp[i+1][j-1]*2 + 2
                elif lo == hi:
                    dp[i][j] = dp[i+1][j-1]*2 + 1
                else:
                    dp[i][j] = dp[i+1][j-1]*2 - dp[lo+1][hi-1]
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            dp[i][j] = dp[i][j] % MOD
    return dp[0][n-1]

if __name__ == "__main__":
    print(count_palindromic_subsequences("bccb"))  # 6
    print(count_palindromic_subsequences("abcd"))  # 4
