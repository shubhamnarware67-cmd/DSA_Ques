"""
Q123: Minimum Window Substring (Sliding Window)
================================================
Problem: Given strings s and t, return the minimum window substring of s
which contains all characters in t. Return "" if none exists.

Example:
    s="ADOBECODEBANC", t="ABC" -> "BANC"
    s="a", t="a"               -> "a"
"""
from collections import Counter

def min_window(s, t):
    if not t or not s: return ""
    need = Counter(t)
    missing = len(t)
    best = ""
    left = 0
    for right, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        while missing == 0:
            window = s[left:right+1]
            if not best or len(window) < len(best):
                best = window
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return best

if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                 # "a"
    print(min_window("a", "aa"))                # ""
