"""
Q365: Largest Perimeter Triangle (Greedy)
==========================================
Problem: Given array of lengths, find largest perimeter of a triangle.
Return 0 if impossible. Triangle inequality: a+b > c.

Example:
    [2,1,2]     -> 5
    [1,2,1,10]  -> 0
    [3,6,2,3]   -> 8
"""

def largest_perimeter(nums):
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0

if __name__ == "__main__":
    print(largest_perimeter([2,1,2]))     # 5
    print(largest_perimeter([1,2,1,10]))  # 0
    print(largest_perimeter([3,6,2,3]))   # 8
