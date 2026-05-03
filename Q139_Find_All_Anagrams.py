"""
Q139: Find All Anagrams in a String (Sliding Window)
======================================================
Problem: Given strings s and p, find all start indices where p's
anagrams appear in s.

Example:
    s="cbaebabacd", p="abc" -> [0,6]
    s="abab", p="ab"        -> [0,1,2]
"""
from collections import Counter

def find_anagrams(s, p):
    if len(p) > len(s): return []
    p_count = Counter(p)
    window = Counter(s[:len(p)])
    result = [0] if window == p_count else []
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left = s[i - len(p)]
        window[left] -= 1
        if window[left] == 0: del window[left]
        if window == p_count: result.append(i - len(p) + 1)
    return result

if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # [0,6]
    print(find_anagrams("abab", "ab"))          # [0,1,2]
