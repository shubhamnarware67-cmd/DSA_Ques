"""
Q446: Number of Ways to Stay in the Same Place After Some Steps (DP)
=======================================================================
Problem: Pointer starts at 0 on array of arrLen. Each step: move left,
right, or stay. Count ways to return to 0 after steps moves.

Example:
    steps=3, arrLen=2 -> 4
    steps=2, arrLen=4 -> 2
"""

def num_ways(steps, arrLen):
    MOD = 10**9 + 7
    max_pos = min(steps // 2, arrLen - 1)
    dp = [0] * (max_pos + 1)
    dp[0] = 1
    for _ in range(steps):
        new_dp = [0] * (max_pos + 1)
        for pos in range(max_pos + 1):
            val = dp[pos]
            if val == 0: continue
            new_dp[pos] = (new_dp[pos] + val) % MOD
            if pos > 0: new_dp[pos-1] = (new_dp[pos-1] + val) % MOD
            if pos < max_pos: new_dp[pos+1] = (new_dp[pos+1] + val) % MOD
        dp = new_dp
    return dp[0]

if __name__ == "__main__":
    print(num_ways(3, 2))  # 4
    print(num_ways(2, 4))  # 2
    print(num_ways(4, 2))  # 8
