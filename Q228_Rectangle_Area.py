"""
Q228: Rectangle Area (Geometry)
=================================
Problem: Given coordinates of two axis-aligned rectangles, return
total area covered by both rectangles.

Example:
    ax1=-3,ay1=0,ax2=3,ay2=4,bx1=0,by1=-1,bx2=9,by2=2 -> 45
"""

def compute_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    area1 = (ax2-ax1)*(ay2-ay1)
    area2 = (bx2-bx1)*(by2-by1)
    # Overlap
    overlap_x = min(ax2, bx2) - max(ax1, bx1)
    overlap_y = min(ay2, by2) - max(ay1, by1)
    overlap = max(0, overlap_x) * max(0, overlap_y)
    return area1 + area2 - overlap

if __name__ == "__main__":
    print(compute_area(-3,0,3,4,0,-1,9,2))  # 45
    print(compute_area(-2,-2,2,2,-2,-2,2,2))  # 16
