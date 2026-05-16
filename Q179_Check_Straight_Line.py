"""
Q179: Check If It Is a Straight Line
======================================
Problem: Given array of coordinates, check if they all lie on a straight line.

Example:
    [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] -> True
    [[1,1],[2,2],[3,4]]                   -> False
"""

def check_straight_line(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx, dy = x1 - x0, y1 - y0
    for x, y in coordinates[2:]:
        # Cross product to avoid division
        if (x - x0) * dy != (y - y0) * dx:
            return False
    return True

if __name__ == "__main__":
    print(check_straight_line([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # True
    print(check_straight_line([[1,1],[2,2],[3,4]]))                     # False
