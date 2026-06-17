"""
Q309: Stone Game VII (Interval DP)
====================================
Problem: Alice and Bob remove stone from either end, other player scores.
Alice scores when Bob removes, Bob scores when Alice removes.
Maximize Alice's score minus Bob's score.

Example:
    [5,3,1,4,2] -> 6
    [7,90,5,1,100,10,10,2] -> 122
"""
from functools import lru_cache

def stone_game_vii(stones):
    n = len(stones)
    prefix = [0] * (n+1)
    for i, s in enumerate(stones):
        prefix[i+1] = prefix[i] + s

    def range_sum(l, r):
        return prefix[r+1] - prefix[l]

    @lru_cache(None)
    def dp(l, r):
        if l == r: return 0
        # Current player removes left (opponent scores sum[l+1..r])
        # or right (opponent scores sum[l..r-1])
        remove_left  = range_sum(l+1, r) - dp(l+1, r)
        remove_right = range_sum(l, r-1) - dp(l, r-1)
        return max(remove_left, remove_right)

    return dp(0, n-1)

if __name__ == "__main__":
    print(stone_game_vii([5,3,1,4,2]))          # 6
    print(stone_game_vii([7,90,5,1,100,10,10,2]))  # 122
