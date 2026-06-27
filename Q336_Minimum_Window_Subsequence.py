"""
Q336: Minimum Window Subsequence (DP / Two Pointers)
=====================================================
Problem: Find minimum window in S such that T is a subsequence of it.
Return "" if not possible.

Example:
    S="abcdebdde", T="bde" -> "bcde"
    S="jmeqkyygqjskel", T="mel" -> "mel"
"""

def min_window_subsequence(s, t):
    m, n = len(s), len(t)
    best = ""
    i = 0
    while i < m:
        j = 0
        while i < m and j < n:
            if s[i] == t[j]: j += 1
            i += 1
        if j == n:
            end = i
            j = n - 1
            i -= 1
            while j >= 0:
                if s[i] == t[j]: j -= 1
                i -= 1
            i += 1
            window = s[i:end]
            if not best or len(window) < len(best):
                best = window
            i += 1
    return best

if __name__ == "__main__":
    print(min_window_subsequence("abcdebdde", "bde"))       # "bcde"
    print(min_window_subsequence("jmeqkyygqjskel", "mel"))  # "mel"
