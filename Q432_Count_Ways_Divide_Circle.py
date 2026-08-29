"""
Q432: Count Ways to Divide a Circular Group of Chords (Catalan-like DP)
==========================================================================
Problem: 2n points on circle, draw n chords pairing all points without
crossing. Count ways mod 10^9+7.

Example:
    n=1 -> 1
    n=2 -> 2
    n=5 -> 16762
"""

def count_ways_chords(n):
    MOD = 10**9 + 7
    total = 2 * n
    dp = [0] * (total + 1)
    dp[0] = 1
    for points in range(2, total+1, 2):
        for k in range(0, points-1, 2):
            dp[points] = (dp[points] + dp[k]*dp[points-2-k]) % MOD
    return dp[total]

if __name__ == "__main__":
    print(count_ways_chords(1))  # 1
    print(count_ways_chords(2))  # 2
    print(count_ways_chords(5))  # 16762
