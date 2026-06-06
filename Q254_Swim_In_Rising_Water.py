"""
Q254: Swim in Rising Water (Dijkstra / Binary Search + BFS)
============================================================
Problem: n x n grid where grid[i][j] is elevation. At time t you can
swim to adjacent cell if both elevations <= t. Find min time to reach bottom-right.

Example:
    [[0,2],[1,3]] -> 3
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]] -> 16
"""
import heapq

def swim_in_water(grid):
    n = len(grid)
    heap = [(grid[0][0], 0, 0)]
    visited = set([(0,0)])
    while heap:
        t, r, c = heapq.heappop(heap)
        if r == n-1 and c == n-1: return t
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                visited.add((nr,nc))
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

if __name__ == "__main__":
    print(swim_in_water([[0,2],[1,3]]))  # 3
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],
            [11,17,18,19,20],[10,9,8,7,6]]
    print(swim_in_water(grid))  # 16
