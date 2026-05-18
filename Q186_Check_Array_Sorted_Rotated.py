"""
Q186: Check if Array is Sorted and Rotated
============================================
Problem: Given array, return True if it was originally sorted in
non-decreasing order, then rotated some number of positions.

Example:
    [3,4,5,1,2] -> True  (sorted [1,2,3,4,5] rotated)
    [2,1,3,4]   -> False
    [1,2,3]     -> True  (0 rotations)
"""

def check(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            count += 1
        if count > 1:
            return False
    return True

if __name__ == "__main__":
    print(check([3,4,5,1,2]))  # True
    print(check([2,1,3,4]))    # False
    print(check([1,2,3]))      # True
