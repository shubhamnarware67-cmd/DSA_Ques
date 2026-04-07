"""
Q27: Rotate Array
=================
Problem: Given an array, rotate it to the right by k steps.

Example:
    Input:  nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
"""

def rotate(nums, k):
    k = k % len(nums)
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    n = len(nums)
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    print(nums)  # [5,6,7,1,2,3,4]
