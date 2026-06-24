"""
Q315: Integer Break (Math / DP)
=================================
Problem: Break integer n into at least 2 positive integers, maximize product.

Example:
    n=2 -> 1   (1*1)
    n=10 -> 36 (3*3*4)
    n=3  -> 2  (1*2)
"""

def integer_break(n):
    # Math insight: use as many 3s as possible
    if n == 2: return 1
    if n == 3: return 2
    product = 1
    while n > 4:
        product *= 3
        n -= 3
    product *= n  # n is 2, 3, or 4 — all fine
    return product

def integer_break_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
    return dp[n]

if __name__ == "__main__":
    print(integer_break(2))    # 1
    print(integer_break(3))    # 2
    print(integer_break(10))   # 36
    print(integer_break_dp(10)) # 36
