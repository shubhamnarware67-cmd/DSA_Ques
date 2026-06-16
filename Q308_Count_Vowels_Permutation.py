"""
Q308: Count Vowels Permutation (Matrix Exponentiation / DP)
============================================================
Problem: Count strings of length n where:
- 'a' can follow 'e'
- 'e' can follow 'a','i'
- 'i' can follow 'e','o'
- 'o' can follow 'i'
- 'u' can follow 'i','o'

Example:
    n=1 -> 5, n=2 -> 10, n=5 -> 68
"""

def count_vowel_permutation(n):
    MOD = 10**9 + 7
    a = e = i = o = u = 1
    for _ in range(n-1):
        a, e, i, o, u = (e+i+u) % MOD, (a+i) % MOD, (e+o) % MOD, i % MOD, (i+o) % MOD
    return (a+e+i+o+u) % MOD

if __name__ == "__main__":
    print(count_vowel_permutation(1))   # 5
    print(count_vowel_permutation(2))   # 10
    print(count_vowel_permutation(5))   # 68
    print(count_vowel_permutation(144)) # 18208803
