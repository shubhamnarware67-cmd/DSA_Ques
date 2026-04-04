"""
Q1: Two Sum
===========
Problem: Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))         # [1, 2]
    print(two_sum([3, 3], 6))            # [0, 1]
