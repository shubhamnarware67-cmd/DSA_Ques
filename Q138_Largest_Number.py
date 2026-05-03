"""
Q138: Largest Number (Custom Sort)
=====================================
Problem: Given list of non-negative integers, arrange them to form
the largest number.

Example:
    [10,2]      -> "210"
    [3,30,34,5,9] -> "9534330"
"""
from functools import cmp_to_key

def largest_number(nums):
    def compare(a, b):
        if a+b > b+a: return -1
        if a+b < b+a: return 1
        return 0
    strs = sorted([str(n) for n in nums], key=cmp_to_key(compare))
    result = ''.join(strs)
    return '0' if result[0] == '0' else result

if __name__ == "__main__":
    print(largest_number([10,2]))          # "210"
    print(largest_number([3,30,34,5,9]))   # "9534330"
    print(largest_number([0,0]))           # "0"
