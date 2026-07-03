"""
Q370: Count and Say with Custom Rules / Number of Wonderful Substrings
=======================================================================
Problem: Count substrings where at most one letter has odd frequency.
(Uses bitmask to track parity of each of first 10 letters)

Example:
    "aba"   -> 4
    "aabb"  -> 9
    "he"    -> 2
"""

def wonderful_substrings(word):
    count = {0: 1}
    mask = 0
    result = 0
    for c in word:
        mask ^= 1 << (ord(c) - ord('a'))
        # All same parity (mask matches)
        result += count.get(mask, 0)
        # Exactly one character with odd frequency
        for i in range(10):
            result += count.get(mask ^ (1 << i), 0)
        count[mask] = count.get(mask, 0) + 1
    return result

if __name__ == "__main__":
    print(wonderful_substrings("aba"))   # 4
    print(wonderful_substrings("aabb"))  # 9
    print(wonderful_substrings("he"))    # 2
