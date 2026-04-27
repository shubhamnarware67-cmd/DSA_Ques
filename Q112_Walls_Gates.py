"""
Q112: Walls and Gates (Multi-source BFS)
==========================================
Problem: Fill each empty room (INF) with distance to nearest gate (0).
Walls = -1, Gates = 0, Empty = INF.

Example:
    INF  -1   0  INF
    INF  INF  INF -1
    INF  -1  INF  -1
      0  -1  INF  INF
    
    Output (distances to nearest gate filled in)
"""
from collections import deque

INF = 2147483647

def walls_and_gates(rooms):
    if not rooms: return
    rows, cols = len(rooms), len(rooms[0])
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))

if __name__ == "__main__":
    rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]
    walls_and_gates(rooms)
    for row in rooms: print(row)
