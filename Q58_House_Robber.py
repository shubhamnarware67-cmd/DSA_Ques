"""
Q58: House Robber (DP)
======================
Problem: Given array of house values, find max money you can rob
without robbing two adjacent houses.

Example:
    [1,2,3,1] -> 4  (rob 1 and 3)
    [2,7,9,3,1] -> 12 (rob 2, 9, 1)
"""

def rob(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1

if __name__ == "__main__":
    print(rob([1,2,3,1]))    # 4
    print(rob([2,7,9,3,1]))  # 12
