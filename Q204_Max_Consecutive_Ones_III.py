"""
Q204: Max Consecutive Ones III (Sliding Window)
=================================================
Problem: Given binary array and k, return max consecutive 1s if you can
flip at most k 0s.

Example:
    [1,1,1,0,0,0,1,1,1,1,0], k=2 -> 6
    [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3 -> 10
"""

def longest_ones(nums, k):
    left = zeros = result = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

if __name__ == "__main__":
    print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
    print(longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # 10
