"""
Q326: Longest Chunked Palindrome Decomposition (Greedy)
=========================================================
Problem: Divide string s into k parts such that [p1,p2,...,pk,pk,...,p2,p1]
is a valid concatenation. Maximize k.

Example:
    "ghiabcdefhelloadamhelloabcdefghi" -> 7
    "merchant" -> 1
    "antaprezatepzapreanta" -> 11
"""

def longest_decomposition(s):
    if not s: return 0
    n = len(s)
    for i in range(1, n//2 + 1):
        if s[:i] == s[n-i:]:
            return 2 + longest_decomposition(s[i:n-i])
    return 1

if __name__ == "__main__":
    print(longest_decomposition("ghiabcdefhelloadamhelloabcdefghi"))  # 7
    print(longest_decomposition("merchant"))                           # 1
    print(longest_decomposition("antaprezatepzapreanta"))             # 11
    print(longest_decomposition("aaa"))                               # 3
