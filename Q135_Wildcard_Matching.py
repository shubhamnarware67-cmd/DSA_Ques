"""
Q135: Wildcard Pattern Matching (DP)
======================================
Problem: Given string s and pattern p with '?' (any single char)
and '*' (any sequence including empty), check if they match.

Example:
    s="aa", p="a"   -> False
    s="aa", p="*"   -> True
    s="cb", p="?a"  -> False
    s="adceb", p="*a*b" -> True
"""

def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1, n+1):
        if p[j-1] == '*': dp[0][j] = dp[0][j-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]

if __name__ == "__main__":
    print(is_match("aa", "a"))       # False
    print(is_match("aa", "*"))       # True
    print(is_match("adceb","*a*b"))  # True
    print(is_match("cb", "?a"))      # False
