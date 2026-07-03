"""
Q372: Minimum Number of Swaps to Move All Balls to Separate Halves
===================================================================
Problem: String of '0' and '1'. Move all 1s to right, 0s to left
with minimum adjacent swaps.

Example:
    "101"  -> 1
    "100"  -> 2
    "0111" -> 0
"""

def minimum_swaps(s):
    # Count swaps to bring all 1s to the right
    ones = s.count('1')
    window_ones = sum(1 for c in s[:ones] if c == '1')
    max_ones = window_ones
    n = len(s)
    for i in range(ones, n):
        window_ones += (s[i] == '1') - (s[i - ones] == '1')
        max_ones = max(max_ones, window_ones)
    return ones - max_ones

if __name__ == "__main__":
    print(minimum_swaps("101"))   # 1
    print(minimum_swaps("100"))   # 2
    print(minimum_swaps("0111"))  # 0
