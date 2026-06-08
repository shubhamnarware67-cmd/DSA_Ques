"""
Q264: Minimum Number of Arrows to Burst Balloons (Greedy)
===========================================================
Problem: Balloons on x-axis with [xstart,xend]. Arrows shot vertically
burst all balloons they pass through. Find min arrows needed.

Example:
    [[10,16],[2,8],[1,6],[7,12]] -> 2
    [[1,2],[3,4],[5,6],[7,8]]    -> 4
    [[1,2],[2,3],[3,4],[4,5]]    -> 2
"""

def find_min_arrow_shots(points):
    if not points: return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    for start, finish in points[1:]:
        if start > end:
            arrows += 1
            end = finish
    return arrows

if __name__ == "__main__":
    print(find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]))  # 2
    print(find_min_arrow_shots([[1,2],[3,4],[5,6],[7,8]]))     # 4
    print(find_min_arrow_shots([[1,2],[2,3],[3,4],[4,5]]))     # 2
