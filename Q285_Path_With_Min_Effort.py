"""
Q285: Path With Minimum Effort (Dijkstra / Binary Search + BFS)
================================================================
Problem: Route in 2D grid. Effort = max absolute difference between
adjacent cells along path. Find min effort path from top-left to bottom-right.

Example:
    [[1,2,2],[3,8,2],[5,3,5]] -> 2
    [[1,2,3],[3,8,4],[5,3,5]] -> 1
"""
import heapq

def minimum_effort_path(heights):
    rows, cols = len(heights), len(heights[0])
    dist = [[float('inf')]*cols for _ in range(rows)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (effort, row, col)
    while heap:
        effort, r, c = heapq.heappop(heap)
        if r == rows-1 and c == cols-1: return effort
        if effort > dist[r][c]: continue
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols:
                new_effort = max(effort, abs(heights[nr][nc]-heights[r][c]))
                if new_effort < dist[nr][nc]:
                    dist[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

if __name__ == "__main__":
    print(minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]))  # 2
    print(minimum_effort_path([[1,2,3],[3,8,4],[5,3,5]]))  # 1
    print(minimum_effort_path([[1,10,6,7,9,10],[1,10,6,7,9,10]]))  # 10
