"""
Q73: Search in Rotated Sorted Array
=====================================
Problem: A sorted array is rotated at some pivot. Search for target.
Return index if found, else -1. Must be O(log n).

Example:
    nums=[4,5,6,7,0,1,2], target=0 -> 4
    nums=[4,5,6,7,0,1,2], target=3 -> -1
"""

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))  # 4
    print(search([4,5,6,7,0,1,2], 3))  # -1
    print(search([1], 0))               # -1
