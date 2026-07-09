"""
Q384: Count Subarrays With Fixed Bounds (Sliding Window)
=========================================================
Problem: Count subarrays where min == minK and max == maxK.

Example:
    nums=[1,3,5,2,7,5], minK=1, maxK=5 -> 2
    nums=[1,1,1,1], minK=1, maxK=1     -> 10
"""

def count_subarrays(nums, minK, maxK):
    result = 0
    min_pos = max_pos = bad_pos = -1
    for i, v in enumerate(nums):
        if v < minK or v > maxK:
            bad_pos = i
        if v == minK: min_pos = i
        if v == maxK: max_pos = i
        # Subarrays ending at i with both min and max
        result += max(0, min(min_pos, max_pos) - bad_pos)
    return result

if __name__ == "__main__":
    print(count_subarrays([1,3,5,2,7,5], 1, 5))  # 2
    print(count_subarrays([1,1,1,1], 1, 1))        # 10
