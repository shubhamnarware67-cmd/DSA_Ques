"""
Q272: Cherry Pickup (Two-Pass DP)
===================================
Problem: Walk from (0,0) to (n-1,n-1) then back, collect max cherries.
Cells with -1 are thorns. Once cherry picked, cell becomes 0.

Example:
    [[0,1,-1],[1,0,-1],[1,1,1]] -> 5
"""

def cherry_pickup(grid):
    n = len(grid)
    # Simulate two paths simultaneously (both start at 0,0)
    from functools import lru_cache
    @lru_cache(None)
    def dp(r1, c1, r2):
        c2 = r1 + c1 - r2
        if r1>=n or c1>=n or r2>=n or c2>=n: return float('-inf')
        if grid[r1][c1]==-1 or grid[r2][c2]==-1: return float('-inf')
        if r1==n-1 and c1==n-1: return grid[r1][c1]
        cherries = grid[r1][c1]
        if r1!=r2 or c1!=c2: cherries += grid[r2][c2]
        best = max(dp(r1+1,c1,r2+1), dp(r1,c1+1,r2+1),
                   dp(r1+1,c1,r2), dp(r1,c1+1,r2))
        return cherries + best
    return max(0, dp(0, 0, 0))

if __name__ == "__main__":
    print(cherry_pickup([[0,1,-1],[1,0,-1],[1,1,1]]))  # 5
    print(cherry_pickup([[1,1,-1],[1,-1,1],[-1,1,1]])) # 0
