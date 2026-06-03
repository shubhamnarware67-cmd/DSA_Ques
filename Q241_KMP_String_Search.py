"""
Q241: KMP (Knuth-Morris-Pratt) String Search
==============================================
Problem: Find all occurrences of pattern in text in O(n+m) time.
Uses failure function to skip redundant comparisons.

Example:
    text="AABABDAABABCABAB", pattern="ABABCABAB"
    -> Found at index 6
"""

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0: return [0]
    # Build failure function
    failure = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    # Search
    results = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            results.append(i - m + 1)
            j = failure[j-1]
    return results

if __name__ == "__main__":
    print(kmp_search("AABABDAABABCABAB", "ABABCABAB"))  # [6]
    print(kmp_search("AABAACAADAABAAABAA", "AABA"))     # [0,9,13]
    print(kmp_search("AAAAABAAABA", "AAAA"))             # [0,1]
