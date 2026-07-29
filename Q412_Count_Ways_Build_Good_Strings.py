"""
Q412: Count Ways to Build Good Strings (DP)
=============================================
Problem: Build string using 'append zero' (cost=zero) or 'append one' (cost=one).
Count strings with length in [low, high]. Mod 10^9+7.

Example:
    low=3, high=3, zero=1, one=1 -> 8
    low=2, high=3, zero=1, one=2 -> 5
"""

def count_good_strings(low, high, zero, one):
    MOD = 10**9 + 7
    dp = [0] * (high + 1)
    dp[0] = 1
    result = 0
    for length in range(1, high + 1):
        if length >= zero:
            dp[length] = (dp[length] + dp[length-zero]) % MOD
        if length >= one:
            dp[length] = (dp[length] + dp[length-one]) % MOD
        if length >= low:
            result = (result + dp[length]) % MOD
    return result

if __name__ == "__main__":
    print(count_good_strings(3, 3, 1, 1))  # 8
    print(count_good_strings(2, 3, 1, 2))  # 5
