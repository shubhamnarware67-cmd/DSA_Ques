"""
Q177: Count Negatives in Sorted Matrix
========================================
Problem: Given m x n matrix sorted in non-increasing order row-wise
and column-wise, return count of negative numbers. O(m+n).

Example:
    [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]] -> 8
"""

def count_negatives(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    r, c = 0, cols - 1
    while r < rows and c >= 0:
        if grid[r][c] < 0:
            count += rows - r   # All elements below are also negative
            c -= 1
        else:
            r += 1
    return count

if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(count_negatives(grid))  # 8
    print(count_negatives([[3,2],[1,0]]))  # 0
