"""
Q271: Dungeon Game (DP — Reverse)
===================================
Problem: Knight starts top-left, must reach bottom-right. Each cell has
health gain/loss. Minimum initial health so knight stays alive (>=1).

Example:
    [[-2,-3,3],[-5,-10,1],[10,30,-5]] -> 7
"""

def calculate_minimum_hp(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    dp = [[0]*n for _ in range(m)]
    for r in range(m-1, -1, -1):
        for c in range(n-1, -1, -1):
            if r == m-1 and c == n-1:
                dp[r][c] = max(1, 1 - dungeon[r][c])
            elif r == m-1:
                dp[r][c] = max(1, dp[r][c+1] - dungeon[r][c])
            elif c == n-1:
                dp[r][c] = max(1, dp[r+1][c] - dungeon[r][c])
            else:
                dp[r][c] = max(1, min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c])
    return dp[0][0]

if __name__ == "__main__":
    print(calculate_minimum_hp([[-2,-3,3],[-5,-10,1],[10,30,-5]]))  # 7
    print(calculate_minimum_hp([[0,0]]))   # 1
    print(calculate_minimum_hp([[-3,5]]))  # 4
