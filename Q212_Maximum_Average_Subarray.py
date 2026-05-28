"""
Q212: Maximum Average Subarray I (Fixed Sliding Window)
========================================================
Problem: Find contiguous subarray of length k with maximum average.

Example:
    nums=[1,12,-5,-6,50,3], k=4 -> 12.75  (subarray [12,-5,-6,50]/4)
    nums=[5], k=1               -> 5.0
"""

def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k

if __name__ == "__main__":
    print(find_max_average([1,12,-5,-6,50,3], 4))  # 12.75
    print(find_max_average([5], 1))                  # 5.0
    print(find_max_average([0,4,0,3,2], 1))          # 4.0
