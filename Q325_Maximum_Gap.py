"""
Q325: Maximum Gap (Bucket Sort / Pigeonhole)
=============================================
Problem: Given unsorted array, find maximum difference between successive
elements in sorted form. Must run in O(n) time/space.

Example:
    [3,6,9,1] -> 3
    [10]       -> 0
"""

def maximum_gap(nums):
    if len(nums) < 2: return 0
    n = len(nums)
    lo, hi = min(nums), max(nums)
    if lo == hi: return 0

    bucket_size = max(1, (hi - lo) // (n - 1))
    bucket_count = (hi - lo) // bucket_size + 1
    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

    for num in nums:
        idx = (num - lo) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)

    max_gap = 0
    prev_max = lo
    for b_min, b_max in buckets:
        if b_min == float('inf'): continue
        max_gap = max(max_gap, b_min - prev_max)
        prev_max = b_max
    return max_gap

if __name__ == "__main__":
    print(maximum_gap([3,6,9,1]))  # 3
    print(maximum_gap([10]))        # 0
    print(maximum_gap([1,10000000])) # 9999999
