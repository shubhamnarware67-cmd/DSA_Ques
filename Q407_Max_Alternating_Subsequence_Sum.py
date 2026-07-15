"""
Q407: Maximum Alternating Subsequence Sum (DP)
==============================================
Problem: Alternating subsequence sum = sum of even-indexed elements
minus sum of odd-indexed elements. Maximize over all subsequences.

Example:
    [4,2,5,3]     -> 7  (subsequence [4,2,5]: 4-2+5=7)
    [5,6,7,8,8]   -> 8
    [6,2,1,2,4,5] -> 10
"""

def max_alternating_sum(nums):
    even = odd = 0
    for num in nums:
        even, odd = max(even, odd + num), max(odd, even - num)
    return even

if __name__ == "__main__":
    print(max_alternating_sum([4,2,5,3]))      # 7
    print(max_alternating_sum([5,6,7,8,8]))    # 8
    print(max_alternating_sum([6,2,1,2,4,5]))  # 10
