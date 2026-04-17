"""
Q71: Regular Expression Matching (DP)
======================================
Problem: Implement regex matching with '.' (any char) and '*' (zero or more).
Return True if the pattern matches the entire string.

Example:
    s="aa", p="a"   -> False
    s="aa", p="a*"  -> True
    s="ab", p=".*"  -> True
"""

def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]

if __name__ == "__main__":
    print(is_match("aa", "a"))    # False
    print(is_match("aa", "a*"))   # True
    print(is_match("ab", ".*"))   # True
    print(is_match("aab", "c*a*b"))  # True
