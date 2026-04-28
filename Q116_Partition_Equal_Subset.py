"""
Q116: Partition Equal Subset Sum (DP / Knapsack variant)
=========================================================
Problem: Given integer array, return True if the array can be partitioned
into two subsets with equal sum.

Example:
    [1,5,11,5] -> True  ([1,5,5] and [11])
    [1,2,3,5]  -> False
"""

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0: return False
    target = total // 2
    dp = {0}
    for num in nums:
        dp = {s + num for s in dp} | dp
        if target in dp: return True
    return target in dp

if __name__ == "__main__":
    print(can_partition([1,5,11,5]))  # True
    print(can_partition([1,2,3,5]))   # False
