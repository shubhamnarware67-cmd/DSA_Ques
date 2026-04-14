"""
Q53: Jump Game (Greedy)
=======================
Problem: Given array where nums[i] is max jump length from position i,
return True if you can reach the last index.

Example:
    [2,3,1,1,4] -> True
    [3,2,1,0,4] -> False
"""

def can_jump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True

if __name__ == "__main__":
    print(can_jump([2,3,1,1,4]))  # True
    print(can_jump([3,2,1,0,4]))  # False
