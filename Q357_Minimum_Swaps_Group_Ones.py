"""
Q357: Minimum Swaps to Group All 1's Together II (Circular Sliding Window)
==========================================================================
Problem: Circular binary array. Find min swaps to group all 1s together.

Example:
    [0,1,0,1,1,0,0] -> 1
    [0,1,1,1,0,0,1,1,0] -> 2
    [1,1,0,0,1]          -> 0
"""

def min_swaps(nums):
    total_ones = sum(nums)
    if total_ones == 0: return 0
    n = len(nums)
    # Sliding window of size total_ones on circular array
    window_ones = sum(nums[:total_ones])
    max_ones = window_ones
    for i in range(total_ones, n + total_ones):
        window_ones += nums[i % n] - nums[(i - total_ones) % n]
        max_ones = max(max_ones, window_ones)
    return total_ones - max_ones

if __name__ == "__main__":
    print(min_swaps([0,1,0,1,1,0,0]))       # 1
    print(min_swaps([0,1,1,1,0,0,1,1,0]))   # 2
    print(min_swaps([1,1,0,0,1]))            # 0
