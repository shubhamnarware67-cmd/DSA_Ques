"""
Q203: Continuous Subarray Sum (Multiple of k)
===============================================
Problem: Return True if array has a continuous subarray of size >= 2
whose elements sum up to a multiple of k.

Example:
    [23,2,4,6,7], k=6  -> True  ([2,4])
    [23,2,6,4,7], k=6  -> True  ([23,2,6,4,7] sums to 42)
    [23,2,6,4,7], k=13 -> False
"""

def check_subarray_sum(nums, k):
    remainder_map = {0: -1}
    running_sum = 0
    for i, num in enumerate(nums):
        running_sum += num
        remainder = running_sum % k
        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i
    return False

if __name__ == "__main__":
    print(check_subarray_sum([23,2,4,6,7], 6))   # True
    print(check_subarray_sum([23,2,6,4,7], 6))   # True
    print(check_subarray_sum([23,2,6,4,7], 13))  # False
