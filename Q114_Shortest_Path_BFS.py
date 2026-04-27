"""
Q114: Shortest Path in Binary Matrix (BFS)
============================================
Problem: Given n x n binary matrix, return length of shortest clear path
from top-left to bottom-right (8-directional). Return -1 if no path.
Clear path: only 0-valued cells.

Example:
    [[0,1],[1,0]] -> 2
    [[0,0,0],[1,1,0],[1,1,0]] -> 4
"""
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]: return -1
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    while queue:
        r, c, dist = queue.popleft()
        if r == n-1 and c == n-1: return dist
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and not grid[nr][nc]:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist+1))
    return -1

if __name__ == "__main__":
    print(shortest_path_binary_matrix([[0,1],[1,0]]))       # 2
    print(shortest_path_binary_matrix([[0,0,0],[1,1,0],[1,1,0]]))  # 4
