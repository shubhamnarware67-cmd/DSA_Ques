"""
Q244: Manacher's Algorithm (Longest Palindromic Substring in O(n))
===================================================================
Problem: Find longest palindromic substring in O(n) using Manacher's algorithm.
Much faster than the O(n²) expand-from-center approach.

Example:
    "babad"    -> "bab" or "aba" (length 3)
    "cbbd"     -> "bb" (length 2)
    "racecar"  -> "racecar" (length 7)
"""

def manacher(s):
    # Transform: "abc" -> "#a#b#c#"
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i] = radius of longest palindrome centered at i
    center = right = 0
    for i in range(n):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        while i-p[i]-1 >= 0 and i+p[i]+1 < n and t[i-p[i]-1] == t[i+p[i]+1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    max_len_idx = p.index(max(p))
    start = (max_len_idx - p[max_len_idx]) // 2
    return s[start:start+p[max_len_idx]]

if __name__ == "__main__":
    print(manacher("babad"))    # "bab"
    print(manacher("cbbd"))     # "bb"
    print(manacher("racecar"))  # "racecar"
    print(manacher("abacaba"))  # "abacaba"
