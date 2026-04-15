"""
Q55: Single Number (XOR Trick)
================================
Problem: Given a non-empty array where every element appears twice
except for one, find that single one. O(n) time, O(1) space.

Example:
    [4,1,2,1,2] -> 4
    [2,2,1]     -> 1
"""

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    print(single_number([4,1,2,1,2]))  # 4
    print(single_number([2,2,1]))      # 1
    print(single_number([1]))          # 1
