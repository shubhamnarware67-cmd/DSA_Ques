"""
Q263: Jump Game VI (DP + Deque for Max in Window)
===================================================
Problem: Jump from index 0 to n-1 with max k steps. Forbidden positions
can't be landed on. Find min jumps or -1 if impossible.

Actually: dp[i] = max(dp[i-k..i-1]) + nums[i]  using sliding window.

Example:
    nums=[1,-1,-2,4,-7,3], k=2 -> 7
    nums=[10,-5,-2,4,0,3], k=3 -> 17
"""
from collections import deque

def max_result(nums, k):
    n = len(nums)
    dp = [float('-inf')] * n
    dp[0] = nums[0]
    dq = deque([0])
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = dp[dq[0]] + nums[i]
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
    return dp[-1]

if __name__ == "__main__":
    print(max_result([1,-1,-2,4,-7,3], 2))   # 7
    print(max_result([10,-5,-2,4,0,3], 3))   # 17
    print(max_result([1,-5,-20,4,-1,3,-6,-3], 2))  # 0
