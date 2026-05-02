"""
Q136: Jump Game II (Greedy - Min Jumps)
=========================================
Problem: Given array, reach last index in minimum number of jumps.
(Guaranteed you can reach the end)

Example:
    [2,3,1,1,4] -> 2  (index 0->1->4)
    [2,3,0,1,4] -> 2
"""

def jump(nums):
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

if __name__ == "__main__":
    print(jump([2,3,1,1,4]))  # 2
    print(jump([2,3,0,1,4]))  # 2
    print(jump([1,2,3]))      # 2
