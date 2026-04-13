"""
Q47: Sliding Window Maximum
============================
Problem: Given an integer array and a sliding window of size k,
return the max values in each window position.

Example:
    nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
"""
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # Stores indices, decreasing order
    result = []
    for i, num in enumerate(nums):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

if __name__ == "__main__":
    print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
    print(max_sliding_window([1], 1))                    # [1]
