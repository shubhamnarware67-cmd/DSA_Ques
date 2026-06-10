"""
Q274: Palindrome Partitioning II (Min Cuts)
============================================
Problem: Given string s, partition such that every substring is a palindrome.
Return minimum cuts needed for such a partition.

Example:
    "aab"    -> 1  ("aa"|"b")
    "a"      -> 0
    "ab"     -> 1
"""

def min_cut(s):
    n = len(s)
    is_pal = [[False]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i, n):
            is_pal[i][j] = s[i]==s[j] and (j-i<=2 or is_pal[i+1][j-1])
    dp = list(range(-1, n))  # dp[i] = min cuts for s[0:i+1]
    for i in range(n):
        for j in range(i+1):
            if is_pal[j][i]:
                dp[i+1] = min(dp[i+1], dp[j]+1)
    return dp[n]

if __name__ == "__main__":
    print(min_cut("aab"))         # 1
    print(min_cut("a"))           # 0
    print(min_cut("ababababab"))   # 1 (entire string?)
    print(min_cut("ab"))          # 1
