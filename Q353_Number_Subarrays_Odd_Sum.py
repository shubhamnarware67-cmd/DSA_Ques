"""
Q353: Number of Sub-arrays with Odd Sum (Prefix Sum Parity)
============================================================
Problem: Count subarrays with odd sum. Return answer mod 10^9+7.

Example:
    [1,3,5]   -> 4
    [2,4,6]   -> 0
    [1,2,3,4,5,6,7] -> 16
"""

def num_odd_sum_subarrays(arr):
    MOD = 10**9 + 7
    odd = even = 0
    even = 1  # prefix sum 0 is even
    result = 0
    prefix = 0
    for num in arr:
        prefix += num
        if prefix % 2 == 0:
            result += odd
            even += 1
        else:
            result += even
            odd += 1
    return result % MOD

if __name__ == "__main__":
    print(num_odd_sum_subarrays([1,3,5]))          # 4
    print(num_odd_sum_subarrays([2,4,6]))          # 0
    print(num_odd_sum_subarrays([1,2,3,4,5,6,7]))  # 16
