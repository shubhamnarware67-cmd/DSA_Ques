"""
Q376: Optimal Binary Search Tree (Interval DP)
===============================================
Problem: Given sorted keys with search probabilities, build BST minimizing
expected search cost.

Example:
    keys=[10,12,20], p=[0.34,0.33,0.33] -> 2.0 (cost with key 12 as root)
"""
from functools import lru_cache

def optimal_bst(keys, prob):
    n = len(keys)
    prefix = [0.0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + prob[i]

    def w(i, j):  # Sum of probabilities from i to j (0-indexed)
        return prefix[j+1] - prefix[i]

    @lru_cache(None)
    def dp(i, j):
        if i > j: return 0.0
        if i == j: return prob[i]
        weight = w(i, j)
        return min(dp(i,k-1) + dp(k+1,j) for k in range(i,j+1)) + weight

    return round(dp(0, n-1), 6)

if __name__ == "__main__":
    keys = [10, 12, 20]
    prob = [0.34, 0.33, 0.33]
    print(optimal_bst(keys, prob))  # ~1.0 (each root gives same cost here)

    keys2 = [10, 20, 30, 40]
    prob2 = [3/16, 3/16, 1/16, 9/16]
    print(optimal_bst(keys2, prob2))  # optimal cost
