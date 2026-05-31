"""
Q222: Number of Distinct Islands (DFS + Shape Encoding)
=========================================================
Problem: Count number of distinct island shapes. Islands with same
shape (even translated) count as one.

Example:
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    -> 1  (both are 2x2 squares)
"""

def num_distinct_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    shapes = set()

    def dfs(r, c, r0, c0, path):
        if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r,c) in seen:
            return
        seen.add((r,c))
        path.append((r-r0, c-c0))
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r+dr, c+dc, r0, c0, path)
        path.append((None,None))  # Backtrack marker

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1 and (r,c) not in seen:
                path = []
                dfs(r, c, r, c, path)
                shapes.add(tuple(path))
    return len(shapes)

if __name__ == "__main__":
    grid1 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(num_distinct_islands(grid1))  # 1

    grid2 = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    print(num_distinct_islands(grid2))  # 3
