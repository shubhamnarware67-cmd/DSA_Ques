"""
Q19: Valid Anagram
==================
Problem: Given two strings s and t, return True if t is an anagram of s,
and False otherwise. An anagram uses all original letters exactly once.

Example:
    "anagram", "nagaram" -> True
    "rat", "car"         -> False
"""
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def is_anagram_v2(s, t):
    if len(s) != len(t):
        return False
    count = [0] * 26
    for a, b in zip(s, t):
        count[ord(a) - ord('a')] += 1
        count[ord(b) - ord('a')] -= 1
    return all(c == 0 for c in count)

if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram_v2("listen", "silent")) # True
