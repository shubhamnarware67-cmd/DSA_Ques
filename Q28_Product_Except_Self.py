"""
Q28: Product of Array Except Self
===================================
Problem: Given an integer array, return an array such that answer[i]
is equal to the product of all elements except nums[i].
No division allowed, O(n) time.

Example:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3])) # [0, 0, 3, 0]
