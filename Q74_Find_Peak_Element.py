"""
Q74: Find Peak Element (Binary Search)
========================================
Problem: A peak element is greater than its neighbors. Given array,
find any peak element and return its index. O(log n).

Example:
    [1,2,3,1] -> 2  (nums[2]=3 is peak)
    [1,2,1,3,5,6,4] -> 5 (nums[5]=6)
"""

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    print(find_peak_element([1,2,3,1]))       # 2
    print(find_peak_element([1,2,1,3,5,6,4])) # 5
