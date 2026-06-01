"""
Q229: Convex Hull (Graham Scan)
=================================
Problem: Find convex hull of a set of 2D points.
Convex hull = smallest convex polygon containing all points.

Example:
    points = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)]
    Hull: [(0,0),(3,1),(4,4),(0,3)]
"""

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1: return points

    def cross(O, A, B):
        return (A[0]-O[0])*(B[1]-O[1]) - (A[1]-O[1])*(B[0]-O[0])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

if __name__ == "__main__":
    pts = [(0,3),(1,1),(2,2),(4,4),(0,0),(1,2),(3,1),(3,3)]
    print("Convex Hull:", convex_hull(pts))
