"""
Q411: Number of Good Ways to Split a String
=============================================
Problem: Split s into left/right such that number of distinct chars
in left equals right. Count such good splits.

Example:
    "aacaba" -> 2
    "abcd"   -> 1
    "aaaaa"  -> 4
"""

def num_splits(s):
    n = len(s)
    left_distinct = [0] * n
    seen = set()
    for i in range(n):
        seen.add(s[i])
        left_distinct[i] = len(seen)

    right_distinct = [0] * n
    seen = set()
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        right_distinct[i] = len(seen)

    count = 0
    for i in range(n-1):
        if left_distinct[i] == right_distinct[i+1]:
            count += 1
    return count

if __name__ == "__main__":
    print(num_splits("aacaba"))  # 2
    print(num_splits("abcd"))    # 1
    print(num_splits("aaaaa"))   # 4
