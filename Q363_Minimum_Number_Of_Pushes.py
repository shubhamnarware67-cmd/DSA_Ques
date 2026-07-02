"""
Q363: Minimum Number of Pushes to Type Word II (Greedy)
========================================================
Problem: Phone keypad with 8 keys (2-9). Assign letters to keys.
First letter on key = 1 push, second = 2, etc. Minimize total pushes.

Example:
    "abcde"      -> 5  (one push each)
    "xyzxyzxyzxyz" -> 12 (x,y,z each appear 4 times; 3 keys each cost 1 push)
    "aabbccddeeffgghhiiiiii" -> 24
"""
from collections import Counter

def minimum_pushes(word):
    freq = sorted(Counter(word).values(), reverse=True)
    result = 0
    for i, f in enumerate(freq):
        result += f * (i // 8 + 1)
    return result

if __name__ == "__main__":
    print(minimum_pushes("abcde"))              # 5
    print(minimum_pushes("xyzxyzxyzxyz"))       # 12
    print(minimum_pushes("aabbccddeeffgghhiiiiii"))  # 24
