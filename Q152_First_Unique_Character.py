"""
Q152: First Unique Character in a String
==========================================
Problem: Given string s, find the first non-repeating character
and return its index. Return -1 if none.

Example:
    "leetcode" -> 0  ('l')
    "loveleetcode" -> 2 ('v')
    "aabb" -> -1
"""
from collections import Counter

def first_uniq_char(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    print(first_uniq_char("leetcode"))     # 0
    print(first_uniq_char("loveleetcode")) # 2
    print(first_uniq_char("aabb"))         # -1
