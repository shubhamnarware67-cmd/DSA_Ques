"""
Q140: Sort Colors (Dutch National Flag Algorithm)
==================================================
Problem: Given array with 0s, 1s, 2s (red, white, blue), sort in-place
in a single pass (O(n) time, O(1) space).

Example:
    [2,0,2,1,1,0] -> [0,0,1,1,2,2]
    [2,0,1]        -> [0,1,2]
"""

def sort_colors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

if __name__ == "__main__":
    a = [2,0,2,1,1,0]; sort_colors(a); print(a)  # [0,0,1,1,2,2]
    b = [2,0,1];        sort_colors(b); print(b)  # [0,1,2]
