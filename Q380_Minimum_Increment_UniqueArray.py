"""
Q380: Minimum Increment to Make Array Unique (Greedy / Counting Sort)
======================================================================
Problem: Find minimum number of increment operations to make all elements unique.

Example:
    [1,2,2]     -> 1   (change one 2 to 3)
    [3,2,1,2,1,7] -> 6
"""

def min_increment_for_unique(nums):
    nums.sort()
    moves = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            moves += nums[i-1] + 1 - nums[i]
            nums[i] = nums[i-1] + 1
    return moves

if __name__ == "__main__":
    print(min_increment_for_unique([1,2,2]))       # 1
    print(min_increment_for_unique([3,2,1,2,1,7])) # 6
