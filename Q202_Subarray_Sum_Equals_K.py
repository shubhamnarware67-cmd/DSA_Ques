"""
Q202: Subarray Sum Equals K (Prefix Sum + HashMap)
====================================================
Problem: Given integer array and k, return total number of continuous
subarrays whose sum equals k.

Example:
    [1,1,1], k=2 -> 2
    [1,2,3], k=3 -> 2  ([1,2] and [3])
"""
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1
    for num in nums:
        prefix += num
        count += seen[prefix - k]
        seen[prefix] += 1
    return count

if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2))  # 2
    print(subarray_sum([1,2,3], 3))  # 2
    print(subarray_sum([1,-1,1], 1)) # 3
