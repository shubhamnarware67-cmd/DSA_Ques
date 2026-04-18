"""
Q75: Decode Ways (DP)
======================
Problem: A message encoded as numbers (1->A, 2->B,...26->Z).
Given a digit string, return the number of ways to decode it.

Example:
    "12" -> 2  ("AB" or "L")
    "226" -> 3 ("BZ","VF","BBF")
    "06" -> 0
"""

def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        one = int(s[i-1])
        two = int(s[i-2:i])
        if one >= 1:
            dp[i] += dp[i-1]
        if 10 <= two <= 26:
            dp[i] += dp[i-2]
    return dp[n]

if __name__ == "__main__":
    print(num_decodings("12"))   # 2
    print(num_decodings("226"))  # 3
    print(num_decodings("06"))   # 0
