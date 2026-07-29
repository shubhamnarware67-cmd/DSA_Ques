"""
Q410: Minimum Replacements to Sort the Array (Greedy)
======================================================
Problem: Replace element with 2+ elements summing to it. Min operations
to make array non-decreasing. Last element unchanged.

Example:
    [3,9,3] -> 2
    [1,2,3,4,5] -> 0
"""

def minimum_replacements(nums):
    n = len(nums)
    ops = 0
    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i+1]: continue
        k = (nums[i] + nums[i+1] - 1) // nums[i+1]
        ops += k - 1
        nums[i] = nums[i] // k
    return ops

if __name__ == "__main__":
    print(minimum_replacements([3,9,3]))      # 2
    print(minimum_replacements([1,2,3,4,5]))  # 0
    print(minimum_replacements([12,9,7,6,17,19,21])) # 6
