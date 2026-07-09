"""
Q385: Longest Continuous Subarray With Absolute Diff <= Limit (Monotonic Deques)
==================================================================================
Problem: Find longest subarray where max-min <= limit.

Example:
    nums=[8,2,4,7], limit=4 -> 2
    nums=[10,1,2,4,7,2], limit=5 -> 4
    nums=[4,2,2,2,4,4,2,2], limit=0 -> 3
"""
from collections import deque

def longest_subarray_limit(nums, limit):
    max_dq = deque()  # Decreasing (max tracker)
    min_dq = deque()  # Increasing (min tracker)
    left = result = 0
    for right, v in enumerate(nums):
        while max_dq and nums[max_dq[-1]] <= v: max_dq.pop()
        while min_dq and nums[min_dq[-1]] >= v: min_dq.pop()
        max_dq.append(right); min_dq.append(right)
        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            left += 1
            if max_dq[0] < left: max_dq.popleft()
            if min_dq[0] < left: min_dq.popleft()
        result = max(result, right - left + 1)
    return result

if __name__ == "__main__":
    print(longest_subarray_limit([8,2,4,7], 4))            # 2
    print(longest_subarray_limit([10,1,2,4,7,2], 5))       # 4
    print(longest_subarray_limit([4,2,2,2,4,4,2,2], 0))    # 3
