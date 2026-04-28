"""
Q117: Target Sum (DP / DFS)
=============================
Problem: Given array and target, assign '+' or '-' to each number.
How many ways can you achieve the target sum?

Example:
    nums=[1,1,1,1,1], target=3 -> 5
"""

def find_target_sum_ways(nums, target):
    from collections import defaultdict
    dp = defaultdict(int)
    dp[0] = 1
    for num in nums:
        new_dp = defaultdict(int)
        for s, count in dp.items():
            new_dp[s + num] += count
            new_dp[s - num] += count
        dp = new_dp
    return dp[target]

if __name__ == "__main__":
    print(find_target_sum_ways([1,1,1,1,1], 3))  # 5
    print(find_target_sum_ways([1], 1))            # 1
