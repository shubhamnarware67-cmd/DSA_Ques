"""
Q307: Minimum Score Triangulation of Polygon (Interval DP)
===========================================================
Problem: Triangulate a convex polygon to minimize product sum of
vertex values of each triangle.

Example:
    [1,2,3]       -> 6    (only one triangle: 1*2*3)
    [3,7,4,5]     -> 144  (triangles: 3*7*5 + 3*4*5 = 105+60=165? 
                           optimal: 3*4*5 + 3*7*4 = 60+84=144)
    [1,3,1,4,1,5] -> 13
"""
from functools import lru_cache

def min_score_triangulation(values):
    n = len(values)
    @lru_cache(None)
    def dp(i, j):
        if j - i < 2: return 0
        return min(values[i]*values[k]*values[j] + dp(i,k) + dp(k,j)
                   for k in range(i+1, j))
    return dp(0, n-1)

if __name__ == "__main__":
    print(min_score_triangulation([1,2,3]))        # 6
    print(min_score_triangulation([3,7,4,5]))      # 144
    print(min_score_triangulation([1,3,1,4,1,5]))  # 13
