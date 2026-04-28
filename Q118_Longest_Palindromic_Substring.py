"""
Q118: Longest Palindromic Substring
=====================================
Problem: Given string s, return the longest palindromic substring.

Example:
    "babad" -> "bab" or "aba"
    "cbbd"  -> "bb"
"""

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res): res = s[l:r+1]
            l -= 1; r += 1
        # Even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res): res = s[l:r+1]
            l -= 1; r += 1
    return res

if __name__ == "__main__":
    print(longest_palindrome("babad"))   # "bab"
    print(longest_palindrome("cbbd"))    # "bb"
    print(longest_palindrome("racecar")) # "racecar"
