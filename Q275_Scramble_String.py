"""
Q275: Scramble String (Memoized Recursion)
===========================================
Problem: A string can be scrambled by splitting into non-empty parts and
optionally swapping them recursively. Check if s2 is a scramble of s1.

Example:
    s1="great", s2="rgeat" -> True
    s1="abcde", s2="caebd" -> False
"""
from functools import lru_cache

def is_scramble(s1, s2):
    @lru_cache(None)
    def dp(a, b):
        if a == b: return True
        if sorted(a) != sorted(b): return False
        n = len(a)
        for i in range(1, n):
            if (dp(a[:i], b[:i]) and dp(a[i:], b[i:])) or \
               (dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i])):
                return True
        return False
    return dp(s1, s2)

if __name__ == "__main__":
    print(is_scramble("great", "rgeat"))  # True
    print(is_scramble("abcde", "caebd"))  # False
    print(is_scramble("a", "a"))          # True
