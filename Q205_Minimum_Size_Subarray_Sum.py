"""
Q205: Minimum Size Subarray Sum (Sliding Window)
=================================================
Problem: Given array of positive integers and target, find minimal length
subarray whose sum >= target. Return 0 if impossible.

Example:
    target=7, nums=[2,3,1,2,4,3] -> 2  ([4,3])
    target=4, nums=[1,4,4]        -> 1  ([4])
"""

def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    print(min_subarray_len(7, [2,3,1,2,4,3]))  # 2
    print(min_subarray_len(4, [1,4,4]))          # 1
    print(min_subarray_len(11, [1,1,1,1,1,1,1,1])) # 0
