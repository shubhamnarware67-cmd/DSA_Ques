"""
Q113: Rotting Oranges (Multi-source BFS)
==========================================
Problem: Grid with 0=empty, 1=fresh orange, 2=rotten orange.
Each minute, rotten oranges infect adjacent fresh ones.
Return minutes until no fresh oranges, or -1 if impossible.

Example:
    [[2,1,1],[1,1,0],[0,1,1]] -> 4
"""
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    max_time = 0
    while queue:
        r, c, t = queue.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                max_time = max(max_time, t+1)
                queue.append((nr, nc, t+1))
    return max_time if fresh == 0 else -1

if __name__ == "__main__":
    print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
    print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
