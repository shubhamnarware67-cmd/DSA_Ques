"""
Q429: Trapping Rain Water II (3D / Heap)
===========================================
Problem: Given m x n heightMap, find volume of water trapped after raining.

Example:
    [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] -> 4
"""
import heapq

def trap_rain_water(heightMap):
    if not heightMap: return 0
    m, n = len(heightMap), len(heightMap[0])
    visited = [[False]*n for _ in range(m)]
    heap = []

    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

    water = 0
    while heap:
        h, r, c = heapq.heappop(heap)
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                visited[nr][nc] = True
                water += max(0, h - heightMap[nr][nc])
                heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))
    return water

if __name__ == "__main__":
    hm = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    print(trap_rain_water(hm))  # 4
