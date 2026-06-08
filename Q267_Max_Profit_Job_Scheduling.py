"""
Q267: Job Scheduling for Maximum Profit (DP + Binary Search)
=============================================================
Problem: Jobs with start, end, profit. Schedule non-overlapping jobs
for maximum profit.

Example:
    startTime=[1,2,3,3], endTime=[3,4,5,6], profit=[50,10,40,70] -> 120
    startTime=[1,2,3,4,6], endTime=[3,5,10,6,9], profit=[20,20,100,200,19] -> 320
"""
import bisect

def job_scheduling(startTime, endTime, profit):
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    ends = [0] + [j[1] for j in jobs]
    dp = [0] * (len(jobs) + 1)
    for i, (s, e, p) in enumerate(jobs, 1):
        idx = bisect.bisect_right(ends, s)
        dp[i] = max(dp[i-1], dp[idx] + p)
    return dp[-1]

if __name__ == "__main__":
    print(job_scheduling([1,2,3,3],[3,4,5,6],[50,10,40,70]))         # 120
    print(job_scheduling([1,2,3,4,6],[3,5,10,6,9],[20,20,100,200,19]))  # 320
