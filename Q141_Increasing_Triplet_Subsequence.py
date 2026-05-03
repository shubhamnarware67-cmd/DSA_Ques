"""
Q141: Increasing Triplet Subsequence (Greedy)
==============================================
Problem: Given integer array, return True if there exist i < j < k
such that nums[i] < nums[j] < nums[k]. O(n) time, O(1) space.

Example:
    [1,2,3,4,5] -> True
    [5,4,3,2,1] -> False
    [2,1,5,0,4,6] -> True
"""

def increasing_triplet(nums):
    first = second = float('inf')
    for num in nums:
        if num <= first: first = num
        elif num <= second: second = num
        else: return True
    return False

if __name__ == "__main__":
    print(increasing_triplet([1,2,3,4,5]))   # True
    print(increasing_triplet([5,4,3,2,1]))   # False
    print(increasing_triplet([2,1,5,0,4,6])) # True
