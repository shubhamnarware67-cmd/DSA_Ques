"""
Q181: Running Sum of 1D Array
================================
Problem: Given array, return running sum where runningSum[i] = sum(nums[0..i]).

Example:
    [1,2,3,4]    -> [1,3,6,10]
    [1,1,1,1,1]  -> [1,2,3,4,5]
    [3,1,2,10,1] -> [3,4,6,16,17]
"""

def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

# Using accumulate
from itertools import accumulate
def running_sum_v2(nums):
    return list(accumulate(nums))

if __name__ == "__main__":
    print(running_sum([1,2,3,4]))     # [1,3,6,10]
    print(running_sum_v2([1,1,1,1,1]))# [1,2,3,4,5]
