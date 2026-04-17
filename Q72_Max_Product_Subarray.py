"""
Q72: Maximum Product Subarray
================================
Problem: Find the contiguous subarray with the largest product.

Example:
    [2,3,-2,4] -> 6   (subarray [2,3])
    [-2,0,-1]  -> 0
"""

def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        max_prod = max(candidates)
        min_prod = min(candidates)
        result = max(result, max_prod)
    return result

if __name__ == "__main__":
    print(max_product([2,3,-2,4]))   # 6
    print(max_product([-2,0,-1]))    # 0
    print(max_product([-2,3,-4]))    # 24
