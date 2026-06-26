"""
Q331: Minimum Cost to Cut a Stick (Interval DP)
=================================================
Problem: Stick of length n, make cuts at positions in array.
Cost of cut = length of stick being cut. Minimize total cost.

Example:
    n=7, cuts=[1,3,4,5] -> 16
    n=9, cuts=[5,6,1,4,2] -> 22
"""
from functools import lru_cache

def min_cost(n, cuts):
    cuts = sorted([0] + cuts + [n])
    m = len(cuts)

    @lru_cache(None)
    def dp(l, r):
        if r - l <= 1: return 0
        return min(cuts[r]-cuts[l] + dp(l,k) + dp(k,r)
                   for k in range(l+1, r))

    return dp(0, m-1)

if __name__ == "__main__":
    print(min_cost(7, [1,3,4,5]))   # 16
    print(min_cost(9, [5,6,1,4,2])) # 22
