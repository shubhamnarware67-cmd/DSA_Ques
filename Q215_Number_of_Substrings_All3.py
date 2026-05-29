"""
Q215: Number of Substrings Containing All Three Characters
===========================================================
Problem: Count substrings of s (containing only a,b,c) that contain
at least one of each.

Example:
    "abcabc" -> 10
    "aaacb"  -> 3
    "abc"    -> 1
"""

def number_of_substrings(s):
    count = 0
    last = {'a': -1, 'b': -1, 'c': -1}
    for i, ch in enumerate(s):
        last[ch] = i
        # All substrings ending at i that start <= min(last values)
        count += 1 + min(last.values())
    return count

if __name__ == "__main__":
    print(number_of_substrings("abcabc"))  # 10
    print(number_of_substrings("aaacb"))   # 3
    print(number_of_substrings("abc"))     # 1
