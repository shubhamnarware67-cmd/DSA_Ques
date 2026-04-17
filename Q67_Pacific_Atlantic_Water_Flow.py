"""
Q67: Pacific Atlantic Water Flow
=================================
Problem: Given m x n matrix of heights, find all cells where rain water
can flow to both Pacific (top/left) and Atlantic (bottom/right) oceans.

Example:
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
"""
from collections import deque

def pacific_atlantic(heights):
    if not heights: return []
    rows, cols = len(heights), len(heights[0])
    def bfs(starts):
        visited = set(starts)
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[r][c]:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        return visited
    pacific = bfs([(0,c) for c in range(cols)] + [(r,0) for r in range(rows)])
    atlantic = bfs([(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(rows)])
    return sorted([list(cell) for cell in pacific & atlantic])

if __name__ == "__main__":
    h = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacific_atlantic(h))
