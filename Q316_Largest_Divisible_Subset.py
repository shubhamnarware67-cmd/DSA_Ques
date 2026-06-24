"""
Q316: Largest Divisible Subset (DP)
=====================================
Problem: Find the largest subset where every pair (a,b) satisfies
a % b == 0 or b % a == 0.

Example:
    [1,2,3]   -> [1,2] or [1,3]
    [1,2,4,8] -> [1,2,4,8]
"""

def largest_divisible_subset(nums):
    if not nums: return []
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    best_len, best_idx = 1, 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > best_len:
            best_len, best_idx = dp[i], i
    result = []
    while best_idx != -1:
        result.append(nums[best_idx])
        best_idx = parent[best_idx]
    return result[::-1]

if __name__ == "__main__":
    print(largest_divisible_subset([1,2,3]))    # [1,2] or [1,3]
    print(largest_divisible_subset([1,2,4,8]))  # [1,2,4,8]
    print(largest_divisible_subset([1,2,3,4,6,24]))  # [1,2,4,24] or similar
