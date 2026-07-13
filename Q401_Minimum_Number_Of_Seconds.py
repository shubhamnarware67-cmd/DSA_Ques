"""
Q401: Minimum Number of Operations to Make Array XOR Sum (Greedy Bit Trick)
============================================================================
Problem: Given array nums and target value k, find minimum number of
bit-flip operations on any element so XOR of array equals k.

Example:
    nums=[2,1,3,4], k=1 -> 2
    nums=[2,0,2,0], k=0 -> 0
"""

def min_operations(nums, k):
    x = 0
    for n in nums:
        x ^= n
    diff = x ^ k
    return bin(diff).count('1')

if __name__ == "__main__":
    print(min_operations([2,1,3,4], 1))  # 2
    print(min_operations([2,0,2,0], 0))  # 0
