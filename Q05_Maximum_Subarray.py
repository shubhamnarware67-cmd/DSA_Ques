"""
Q5: Maximum Subarray (Kadane's Algorithm)
=========================================
Problem: Given an integer array nums, find the contiguous subarray
which has the largest sum and return its sum.

Example:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6
"""

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray([1]))                         # 1
    print(max_subarray([5,4,-1,7,8]))               # 23
