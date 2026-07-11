"""
Q387: Sort Integers by The Power Value (Memoization)
======================================================
Problem: Power of x = steps to reach 1 by Collatz sequence.
Return kth element when integers in [lo,hi] are sorted by power (ties: value).

Example:
    lo=12, hi=15, k=2 -> 13
    lo=7, hi=11, k=4  -> 7
"""
from functools import lru_cache

def get_kth(lo, hi, k):
    @lru_cache(None)
    def power(n):
        if n == 1: return 0
        if n % 2 == 0: return 1 + power(n // 2)
        return 1 + power(3*n + 1)

    nums = sorted(range(lo, hi+1), key=lambda x: (power(x), x))
    return nums[k-1]

if __name__ == "__main__":
    print(get_kth(12, 15, 2))  # 13
    print(get_kth(7, 11, 4))   # 7
    print(get_kth(1, 1, 1))    # 1
