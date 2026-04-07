"""
Q24: Longest Increasing Subsequence (LIS)
==========================================
Problem: Given an integer array, return the length of the longest
strictly increasing subsequence.

Example:
    Input:  [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4  (2, 3, 7, 101)
"""

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# O(n log n) solution using patience sorting
import bisect

def length_of_lis_fast(nums):
    sub = []
    for num in nums:
        pos = bisect.bisect_left(sub, num)
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num
    return len(sub)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis(nums))       # 4
    print(length_of_lis_fast(nums))  # 4
