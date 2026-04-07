"""
Q26: Find the Duplicate Number
================================
Problem: Given an array of n+1 integers where each integer is between 1 and n,
find the one duplicate number. (Floyd's Cycle Detection)

Example:
    Input:  [1, 3, 4, 2, 2]
    Output: 2
"""

def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))  # 2
    print(find_duplicate([3, 1, 3, 4, 2]))  # 3
