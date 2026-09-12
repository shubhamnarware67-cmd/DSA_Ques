"""
Q437: Maximum Equal Frequency (Sliding Window + Frequency Counting)
=====================================================================
Problem: Find longest prefix such that removing exactly one element
makes all remaining elements have equal frequency.

Example:
    [2,2,1,1,5,3,3,5] -> 7
    [1,1,1,2,2,2,3,3,3,4,4,4,5] -> 13
"""
from collections import defaultdict

def max_equal_freq(nums):
    count = defaultdict(int)
    freq_count = defaultdict(int)
    result = 0

    for i, num in enumerate(nums):
        if count[num] > 0:
            freq_count[count[num]] -= 1
        count[num] += 1
        freq_count[count[num]] += 1

        max_freq = max(count.values())
        n = i + 1

        if max_freq == 1:
            result = n
        elif freq_count[max_freq] * max_freq == n - 1:
            result = n
        elif freq_count[max_freq-1] * (max_freq-1) == n - max_freq:
            result = n
    return result

if __name__ == "__main__":
    print(max_equal_freq([2,2,1,1,5,3,3,5]))  # 7
    print(max_equal_freq([1,1,1,2,2,2,3,3,3,4,4,4,5]))  # 13
