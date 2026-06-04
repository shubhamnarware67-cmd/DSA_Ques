"""
Q242: Rabin-Karp String Search (Rolling Hash)
===============================================
Problem: Find pattern in text using rolling hash. Average O(n+m).
Useful when searching multiple patterns simultaneously.

Example:
    text="GEEKS FOR GEEKS", pattern="GEEK" -> [0, 10]
"""

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return []
    BASE, MOD = 256, 101
    h = pow(BASE, m-1, MOD)
    p_hash = t_hash = 0
    results = []

    for i in range(m):
        p_hash = (BASE*p_hash + ord(pattern[i])) % MOD
        t_hash = (BASE*t_hash + ord(text[i])) % MOD

    for i in range(n-m+1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:  # Verify (handle hash collision)
                results.append(i)
        if i < n-m:
            t_hash = (BASE*(t_hash - ord(text[i])*h) + ord(text[i+m])) % MOD
            if t_hash < 0: t_hash += MOD
    return results

if __name__ == "__main__":
    print(rabin_karp("GEEKS FOR GEEKS", "GEEK"))    # [0, 10]
    print(rabin_karp("AABAACAADAABAABA", "AABA"))   # [0, 9, 12]
