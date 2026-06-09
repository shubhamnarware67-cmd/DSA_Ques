"""
Q273: Strange Printer (Interval DP)
=====================================
Problem: A printer prints a sequence of same characters each turn.
Find minimum number of turns to print a string.

Example:
    "aaabbb" -> 2
    "aba"    -> 2
    "tbgtgb" -> 4
"""

def strange_printer(s):
    n = len(s)
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, j):
        if i > j: return 0
        res = 1 + dp(i+1, j)
        for k in range(i+1, j+1):
            if s[k] == s[i]:
                res = min(res, dp(i, k-1) + dp(k+1, j))
        return res
    return dp(0, n-1)

if __name__ == "__main__":
    print(strange_printer("aaabbb"))  # 2
    print(strange_printer("aba"))     # 2
    print(strange_printer("tbgtgb"))  # 4
