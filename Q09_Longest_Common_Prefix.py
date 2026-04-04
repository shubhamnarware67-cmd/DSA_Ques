"""
Q9: Longest Common Prefix
==========================
Problem: Write a function to find the longest common prefix string
amongst an array of strings. Return "" if there is no common prefix.

Example:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
"""

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))  # "fl"
    print(longest_common_prefix(["dog","racecar","car"]))     # ""
