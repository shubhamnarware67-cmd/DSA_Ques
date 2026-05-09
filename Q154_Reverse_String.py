"""
Q154: Reverse String (In-place)
=================================
Problem: Write a function that reverses string s in-place (char array).
Must use O(1) extra memory.

Example:
    ["h","e","l","l","o"] -> ["o","l","l","e","h"]
    ["H","a","n","n","a","h"] -> ["h","a","n","n","a","H"]
"""

def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1; right -= 1

if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    reverse_string(s1)
    print(s1)  # ["o","l","l","e","h"]

    s2 = ["H","a","n","n","a","h"]
    reverse_string(s2)
    print(s2)  # ["h","a","n","n","a","H"]
