"""
Q383: Maximum Points You Can Obtain from Cards (Sliding Window)
================================================================
Problem: Take k cards from either left or right end. Maximize sum.
Trick: Minimize sum of middle subarray of size n-k.

Example:
    cardPoints=[1,2,3,4,5,6,1], k=3 -> 12
    cardPoints=[2,2,2], k=2          -> 4
"""

def max_score(cardPoints, k):
    n = len(cardPoints)
    window_size = n - k
    if window_size == 0: return sum(cardPoints)
    window_sum = sum(cardPoints[:window_size])
    min_sum = window_sum
    for i in range(window_size, n):
        window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_sum = min(min_sum, window_sum)
    return sum(cardPoints) - min_sum

if __name__ == "__main__":
    print(max_score([1,2,3,4,5,6,1], 3))   # 12
    print(max_score([2,2,2], 2))             # 4
    print(max_score([9,7,7,9,7,7,9], 7))    # 55
