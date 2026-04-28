"""
Q120: Group Anagrams
=====================
Problem: Given array of strings, group anagrams together.

Example:
    ["eat","tea","tan","ate","nat","bat"]
    -> [["eat","tea","ate"],["tan","nat"],["bat"]]
"""
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

if __name__ == "__main__":
    result = group_anagrams(["eat","tea","tan","ate","nat","bat"])
    for group in sorted(result, key=len, reverse=True):
        print(sorted(group))
    # ['ate','eat','tea'], ['nat','tan'], ['bat']
