"""
Q134: Burst Balloons (Interval DP)
=====================================
Problem: Given balloons with values, bursting balloon i gives
nums[i-1]*nums[i]*nums[i+1] coins. Maximize coins.

Example:
    [3,1,5,8] -> 167
    (burst 1: 3*1*5=15, burst 5: 3*5*8=120, burst 3: 1*3*8=24, burst 8: 1*8*1=8)
"""

def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left+1, right):
                dp[left][right] = max(dp[left][right],
                    nums[left]*nums[k]*nums[right] + dp[left][k] + dp[k][right])
    return dp[0][n-1]

if __name__ == "__main__":
    print(max_coins([3,1,5,8]))  # 167
    print(max_coins([1,5]))      # 10
