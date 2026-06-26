"""
Q327: Bitwise ORs of Subarrays (DP)
=====================================
Problem: For each subarray, compute the OR. Return number of distinct results.

Example:
    [0]       -> 1
    [1,1,2]   -> 3  ({1},{2},{3})
    [1,2,4]   -> 6
"""

def subarray_bitwise_ors(arr):
    result = set()
    prev = set()
    for num in arr:
        curr = {num | p for p in prev} | {num}
        result |= curr
        prev = curr
    return len(result)

if __name__ == "__main__":
    print(subarray_bitwise_ors([0]))        # 1
    print(subarray_bitwise_ors([1,1,2]))    # 3
    print(subarray_bitwise_ors([1,2,4]))    # 6
