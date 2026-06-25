"""
Q323: Longest Arithmetic Subsequence (DP)
==========================================
Problem: Find length of longest arithmetic subsequence in array.

Example:
    [3,6,9,12]  -> 4
    [9,4,7,2,10] -> 3  ([4,7,10])
    [20,1,15,3,10,5,8] -> 4  ([20,15,10,5])
"""

def longest_arith_seq_length(nums):
    dp = [{} for _ in range(len(nums))]
    result = 2
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[j].get(diff, 1) + 1
            result = max(result, dp[i][diff])
    return result

if __name__ == "__main__":
    print(longest_arith_seq_length([3,6,9,12]))      # 4
    print(longest_arith_seq_length([9,4,7,2,10]))    # 3
    print(longest_arith_seq_length([20,1,15,3,10,5,8])) # 4
