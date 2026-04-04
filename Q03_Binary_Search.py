"""
Q3: Binary Search
=================
Problem: Given a sorted array of integers and a target value,
return the index of target if found, else return -1.

Example:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(binary_search([-1, 0, 3, 5, 9, 12], 2))   # -1
