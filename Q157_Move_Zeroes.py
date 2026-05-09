"""
Q157: Move Zeroes
==================
Problem: Given integer array, move all 0s to the end while maintaining
relative order of non-zero elements. In-place, minimize total operations.

Example:
    [0,1,0,3,12] -> [1,3,12,0,0]
    [0,0,1]       -> [1,0,0]
"""

def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

if __name__ == "__main__":
    a = [0,1,0,3,12]; move_zeroes(a); print(a)  # [1,3,12,0,0]
    b = [0,0,1];       move_zeroes(b); print(b)  # [1,0,0]
