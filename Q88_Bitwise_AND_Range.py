"""
Q88: Bitwise AND of Numbers Range
====================================
Problem: Given range [left, right], return bitwise AND of all numbers.

Example:
    left=5, right=7   -> 4
    left=0, right=0   -> 0
    left=1, right=2147483647 -> 0
"""

def range_bitwise_and(left, right):
    shift = 0
    while left != right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift

if __name__ == "__main__":
    print(range_bitwise_and(5, 7))   # 4
    print(range_bitwise_and(0, 0))   # 0
    print(range_bitwise_and(1, 2147483647))  # 0
