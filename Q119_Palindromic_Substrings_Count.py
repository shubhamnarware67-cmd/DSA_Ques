"""
Q119: Palindromic Substrings Count
=====================================
Problem: Given string s, return the number of palindromic substrings.

Example:
    "abc" -> 3  (a, b, c)
    "aaa" -> 6  (a,a,a,aa,aa,aaa)
"""

def count_substrings(s):
    count = 0
    for i in range(len(s)):
        # Odd
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1; l -= 1; r += 1
        # Even
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1; l -= 1; r += 1
    return count

if __name__ == "__main__":
    print(count_substrings("abc"))  # 3
    print(count_substrings("aaa"))  # 6
