"""
Q227: Max Points on a Line
============================
Problem: Given array of points, return maximum number of points
that lie on the same straight line.

Example:
    [[1,1],[2,2],[3,3]]      -> 3
    [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]] -> 4
"""
from collections import defaultdict
from math import gcd

def max_points(points):
    n = len(points)
    if n <= 2: return n
    result = 2
    for i in range(n):
        slopes = defaultdict(int)
        for j in range(i+1, n):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            if dx == 0: slope = ('inf', 0)
            else:
                g = gcd(abs(dx), abs(dy))
                slope = (dy//g, dx//g)
            slopes[slope] += 1
            result = max(result, slopes[slope] + 1)
    return result

if __name__ == "__main__":
    print(max_points([[1,1],[2,2],[3,3]]))  # 3
    print(max_points([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))  # 4
