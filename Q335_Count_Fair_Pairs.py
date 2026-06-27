"""
Q335: Count Fair Pairs (Two Pointers + Binary Search)
======================================================
Problem: Count pairs (i,j) where i<j and lower <= nums[i]+nums[j] <= upper.

Example:
    nums=[0,1,7,4,4,5], lower=3, upper=6  -> 6
    nums=[1,7,9,2,5],   lower=11, upper=11 -> 1
"""
import bisect

def count_fair_pairs(nums, lower, upper):
    nums.sort()
    count = 0
    n = len(nums)
    for i in range(n-1):
        lo = bisect.bisect_left(nums, lower - nums[i], i+1)
        hi = bisect.bisect_right(nums, upper - nums[i], i+1)
        count += hi - lo
    return count

if __name__ == "__main__":
    print(count_fair_pairs([0,1,7,4,4,5], 3, 6))   # 6
    print(count_fair_pairs([1,7,9,2,5], 11, 11))    # 1
