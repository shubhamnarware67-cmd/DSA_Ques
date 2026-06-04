"""
Q243: Z Algorithm (Pattern Matching)
======================================
Problem: Build Z-array where Z[i] is length of longest substring starting
at i that is also a prefix of the string. Use for pattern matching in O(n+m).

Example:
    pattern="aabxaa", text="aabxaaabxaabxaa"
    -> Pattern found at index 7
"""

def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r-i, z[i-l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

def z_search(text, pattern):
    combined = pattern + '$' + text
    z = z_algorithm(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m+1, len(combined)) if z[i] == m]

if __name__ == "__main__":
    print(z_algorithm("aabxaa"))    # [6,1,0,0,2,1]
    print(z_search("aabxaaabxaabxaa", "aabxaa"))  # [0,7,9]
