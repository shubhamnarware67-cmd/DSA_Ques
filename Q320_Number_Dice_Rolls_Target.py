"""
Q320: Number of Dice Rolls With Target Sum (DP)
=================================================
Problem: n dice each with k faces (1 to k). Count ways to roll sum = target.

Example:
    n=1, k=6, target=3 -> 1
    n=2, k=6, target=7 -> 6
    n=30, k=30, target=500 -> 222616187
"""

def num_rolls_to_target(n, k, target):
    MOD = 10**9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(n):
        new_dp = [0] * (target + 1)
        for s in range(target + 1):
            if dp[s] == 0: continue
            for face in range(1, k+1):
                if s + face <= target:
                    new_dp[s+face] = (new_dp[s+face] + dp[s]) % MOD
        dp = new_dp
    return dp[target]

if __name__ == "__main__":
    print(num_rolls_to_target(1, 6, 3))       # 1
    print(num_rolls_to_target(2, 6, 7))       # 6
    print(num_rolls_to_target(30, 30, 500))   # 222616187
