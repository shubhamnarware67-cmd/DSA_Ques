"""
Q146: Contains Duplicate / Nearby Duplicate
=============================================
Problem 1: Return True if any value appears at least twice.
Problem 2: Return True if nums[i]==nums[j] and abs(i-j) <= k.

Example:
    [1,2,3,1]            -> True
    [1,2,3,4]            -> False
    [1,2,3,1,2,3], k=2   -> False
    [1,0,1,1], k=1       -> True
"""

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

def contains_nearby_duplicate(nums, k):
    window = {}
    for i, num in enumerate(nums):
        if num in window and i - window[num] <= k:
            return True
        window[num] = i
    return False

if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))           # True
    print(contains_duplicate([1,2,3,4]))           # False
    print(contains_nearby_duplicate([1,2,3,1,2,3],2))  # False
    print(contains_nearby_duplicate([1,0,1,1],1))      # True
