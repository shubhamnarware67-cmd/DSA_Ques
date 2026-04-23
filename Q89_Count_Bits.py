"""
Q89: Counting Bits (DP)
========================
Problem: Given integer n, return array of length n+1 where ans[i]
is the number of 1s in binary representation of i.

Example:
    n=2 -> [0,1,1]
    n=5 -> [0,1,1,2,1,2]
"""

def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

if __name__ == "__main__":
    print(count_bits(2))  # [0,1,1]
    print(count_bits(5))  # [0,1,1,2,1,2]
