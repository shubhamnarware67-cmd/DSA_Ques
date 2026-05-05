"""
Q149: Sort Array by Increasing Frequency
==========================================
Problem: Sort array in increasing order of frequency. For equal frequency,
sort in decreasing order of value.

Example:
    [1,1,2,2,2,3]    -> [3,1,1,2,2,2]
    [2,3,1,3,2]      -> [1,3,3,2,2]
    [-1,1,-6,4,5,-6,1,4,1] -> [5,-1,4,4,-6,-6,1,1,1]
"""
from collections import Counter

def frequency_sort(nums):
    count = Counter(nums)
    return sorted(nums, key=lambda x: (count[x], -x))

if __name__ == "__main__":
    print(frequency_sort([1,1,2,2,2,3]))           # [3,1,1,2,2,2]
    print(frequency_sort([2,3,1,3,2]))             # [1,3,3,2,2]
    print(frequency_sort([-1,1,-6,4,5,-6,1,4,1])) # [5,-1,4,4,-6,-6,1,1,1]
