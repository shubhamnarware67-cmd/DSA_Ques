"""
Q32: Longest Substring Without Repeating Characters
====================================================
Problem: Given a string s, find the length of the longest substring
without repeating characters. (Sliding Window)

Example:
    "abcabcbb" -> 3  ("abc")
    "bbbbb"    -> 1  ("b")
    "pwwkew"   -> 3  ("wke")
"""

def length_of_longest_substring(s):
    char_index = {}
    max_len = left = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
