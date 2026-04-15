"""
Q57: Missing Number
===================
Problem: Given array containing n distinct numbers in range [0, n],
return the only number missing.

Example:
    [3,0,1]   -> 2
    [9,6,4,2,3,5,7,0,1] -> 8
"""

def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

def missing_number_xor(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

if __name__ == "__main__":
    print(missing_number([3,0,1]))              # 2
    print(missing_number_xor([9,6,4,2,3,5,7,0,1]))  # 8
