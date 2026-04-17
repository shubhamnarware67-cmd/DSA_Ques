"""
Q69: Minimum Path Sum (DP)
===========================
Problem: Given m x n grid filled with non-negative numbers, find a path
from top-left to bottom-right (only right/down moves) with minimum sum.

Example:
    [[1,3,1],[1,5,1],[4,2,1]] -> 7  (1->3->1->1->1)
"""

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0: continue
            elif r == 0: grid[r][c] += grid[r][c-1]
            elif c == 0: grid[r][c] += grid[r-1][c]
            else: grid[r][c] += min(grid[r-1][c], grid[r][c-1])
    return grid[m-1][n-1]

if __name__ == "__main__":
    print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
