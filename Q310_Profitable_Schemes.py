"""
Q310: Profitable Schemes (3D DP)
==================================
Problem: Group of n members. Crimes need minMembers[i] members and earn
profit[i]. Count schemes using <= n members with profit >= minProfit.

Example:
    n=5, minProfit=3, group=[2,2], profit=[2,3] -> 2
    n=10, minProfit=5, group=[2,3,5], profit=[6,7,8] -> 7
"""

def profitable_schemes(n, minProfit, group, profit):
    MOD = 10**9 + 7
    # dp[members][profit_so_far]
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for g, p in zip(group, profit):
        for members in range(n, g-1, -1):
            for prof in range(minProfit, -1, -1):
                new_prof = min(prof + p, minProfit)
                dp[members][new_prof] = (dp[members][new_prof] + dp[members-g][prof]) % MOD
    return sum(dp[m][minProfit] for m in range(n+1)) % MOD

if __name__ == "__main__":
    print(profitable_schemes(5, 3, [2,2], [2,3]))         # 2
    print(profitable_schemes(10, 5, [2,3,5], [6,7,8]))    # 7
