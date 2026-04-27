"""
Q115: Min Cost Climbing Stairs (DP)
=====================================
Problem: Given cost array for stairs, pay cost[i] to step on stair i.
Then climb 1 or 2 steps. Find minimum cost to reach top (beyond last step).

Example:
    [10,15,20] -> 15
    [1,100,1,1,1,100,1,1,100,1] -> 6
"""

def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[n]

if __name__ == "__main__":
    print(min_cost_climbing_stairs([10,15,20]))                        # 15
    print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))      # 6
