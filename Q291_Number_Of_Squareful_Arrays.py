"""
Q291: Number of Squareful Arrays (Backtracking)
=================================================
Problem: An array is squareful if the sum of every adjacent pair is a perfect square.
Count the number of distinct squareful permutations of nums.

Example:
    [1,17,8]    -> 2  ([1,8,17],[17,8,1])
    [2,2,2]     -> 1
"""
from math import isqrt
from collections import Counter

def num_squareful_perms(nums):
    def is_square(n):
        return isqrt(n)**2 == n

    count = Counter(nums)
    keys = list(count.keys())
    graph = {k: [j for j in keys if is_square(k+j)] for k in keys}
    result = [0]

    def dfs(prev, remaining):
        if remaining == 0:
            result[0] += 1
            return
        for nxt in graph[prev]:
            if count[nxt] > 0:
                count[nxt] -= 1
                dfs(nxt, remaining-1)
                count[nxt] += 1

    for key in keys:
        count[key] -= 1
        dfs(key, len(nums)-1)
        count[key] += 1
    return result[0]

if __name__ == "__main__":
    print(num_squareful_perms([1,17,8]))  # 2
    print(num_squareful_perms([2,2,2]))   # 1
    print(num_squareful_perms([1,1]))     # 1
