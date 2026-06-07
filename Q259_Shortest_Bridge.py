"""
Q259: Shortest Bridge (BFS + DFS)
===================================
Problem: Binary matrix has exactly 2 islands. Find minimum flips to connect them
(i.e. minimum 0-to-1 changes needed to build a bridge).

Example:
    [[0,1],[1,0]] -> 1
    [[0,1,0],[0,0,0],[0,0,1]] -> 2
"""
from collections import deque

def shortest_bridge(grid):
    n = len(grid)
    visited = set()
    queue = deque()

    def dfs(r, c):
        if r<0 or r>=n or c<0 or c>=n or grid[r][c]==0 or (r,c) in visited:
            return
        visited.add((r,c))
        queue.append((r,c,0))
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]: dfs(r+dr,c+dc)

    found = False
    for r in range(n):
        if found: break
        for c in range(n):
            if grid[r][c]==1: dfs(r,c); found=True; break

    while queue:
        r, c, dist = queue.popleft()
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                if grid[nr][nc]==1: return dist
                visited.add((nr,nc))
                queue.append((nr,nc,dist+1))

if __name__ == "__main__":
    print(shortest_bridge([[0,1],[1,0]]))            # 1
    print(shortest_bridge([[0,1,0],[0,0,0],[0,0,1]])) # 2
