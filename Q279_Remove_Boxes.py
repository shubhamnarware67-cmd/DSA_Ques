"""
Q279: Remove Boxes (3D DP)
============================
Problem: Remove boxes to earn points. Remove k consecutive boxes of same
color earns k^2 points. Find maximum points.

Example:
    [1,3,2,2,2,3,4,3,1] -> 23
    [1,1,1]               -> 9
"""
from functools import lru_cache

def remove_boxes(boxes):
    @lru_cache(None)
    def dp(l, r, k):
        if l > r: return 0
        # Extend run of boxes[r] to include boxes before l with same color
        while l < r and boxes[r] == boxes[r-1]:
            r -= 1; k += 1
        res = dp(l, r-1, 0) + (k+1)**2
        for m in range(l, r):
            if boxes[m] == boxes[r]:
                res = max(res, dp(m+1, r-1, 0) + dp(l, m, k+1))
        return res
    return dp(0, len(boxes)-1, 0)

if __name__ == "__main__":
    print(remove_boxes([1,3,2,2,2,3,4,3,1]))  # 23
    print(remove_boxes([1,1,1]))               # 9
    print(remove_boxes([1]))                   # 1
