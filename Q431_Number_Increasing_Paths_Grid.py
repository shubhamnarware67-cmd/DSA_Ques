"""
Q431: Number of Increasing Paths in a Grid (DFS + Memoization)
==================================================================
Problem: Count strictly increasing paths in grid (4-directional).
Return count mod 10^9+7. Single cell counts as length-1 path.

Example:
    [[1,1],[3,4]] -> 8
    [[1],[2]]     -> 3
"""
from functools import lru_cache

def count_paths(grid):
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dfs(r, c):
        total = 1
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n and grid[nr][nc] > grid[r][c]:
                total += dfs(nr, nc)
        return total % MOD

    return sum(dfs(r,c) for r in range(m) for c in range(n)) % MOD

if __name__ == "__main__":
    print(count_paths([[1,1],[3,4]]))  # 8
    print(count_paths([[1],[2]]))      # 3
