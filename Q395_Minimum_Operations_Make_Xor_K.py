"""
Q395: Minimum Operations to Make Array XOR Equal to k (Bit Manipulation)
=========================================================================
Problem: One operation: flip any bit in any element. Find min ops to
make XOR of entire array equal to k.

Example:
    nums=[2,1,3,4], k=1 -> 2
    nums=[2,0,2,0], k=0 -> 0
"""

def min_operations(nums, k):
    current_xor = 0
    for n in nums:
        current_xor ^= n
    diff = current_xor ^ k
    return bin(diff).count('1')

if __name__ == "__main__":
    print(min_operations([2,1,3,4], 1))  # 2
    print(min_operations([2,0,2,0], 0))  # 0
    print(min_operations([1,2,3], 7))    # 1
