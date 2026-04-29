"""
Q124: Longest Repeating Character Replacement (Sliding Window)
===============================================================
Problem: Given string s and integer k, you can replace k characters.
Return length of longest substring with all same characters after replacements.

Example:
    s="AABABBA", k=1 -> 4  ("AABA" or "ABBA")
    s="ABAB", k=2    -> 4
"""

def character_replacement(s, k):
    count = {}
    max_count = result = left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

if __name__ == "__main__":
    print(character_replacement("AABABBA", 1))  # 4
    print(character_replacement("ABAB", 2))      # 4
