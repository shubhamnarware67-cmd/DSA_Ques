"""
Q306: Minimum Operations to Reduce X to Zero (Sliding Window)
==============================================================
Problem: Each op remove leftmost or rightmost element. Find min ops to
make sum of removed elements equal to x. Return -1 if impossible.
Trick: Find longest subarray with sum = total - x.

Example:
    nums=[1,1,4,2,3], x=5   -> 2
    nums=[5,6,7,8,9], x=4   -> -1
    nums=[3,2,20,1,1,3], x=10 -> 5
"""

def min_operations(nums, x):
    target = sum(nums) - x
    if target < 0: return -1
    if target == 0: return len(nums)

    max_len = -1
    curr_sum = left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > target and left <= right:
            curr_sum -= nums[left]; left += 1
        if curr_sum == target:
            max_len = max(max_len, right - left + 1)
    return len(nums) - max_len if max_len != -1 else -1

if __name__ == "__main__":
    print(min_operations([1,1,4,2,3], 5))       # 2
    print(min_operations([5,6,7,8,9], 4))        # -1
    print(min_operations([3,2,20,1,1,3], 10))    # 5
