"""
Q416: Minimum Time Visit All Points (Chebyshev Distance)
==========================================================
Problem: Given points, find min time to visit all (in order).
Moving 1 unit in any of 8 directions takes 1 second.

Example:
    [[1,1],[3,4],[-1,0]] -> 7
    [[3,2],[-2,2]] -> 5
"""

def min_time_to_visit_all_points(points):
    total = 0
    for i in range(1, len(points)):
        dx = abs(points[i][0] - points[i-1][0])
        dy = abs(points[i][1] - points[i-1][1])
        total += max(dx, dy)
    return total

if __name__ == "__main__":
    print(min_time_to_visit_all_points([[1,1],[3,4],[-1,0]]))  # 7
    print(min_time_to_visit_all_points([[3,2],[-2,2]]))         # 5
