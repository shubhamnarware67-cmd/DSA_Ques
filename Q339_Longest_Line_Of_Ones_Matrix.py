"""
Q339: Longest Line of Consecutive 1s in Matrix
================================================
Problem: Given binary matrix, find longest line of consecutive 1s.
Line can be horizontal, vertical, diagonal, or anti-diagonal.

Example:
    [[0,1,1,0],[0,1,1,0],[0,0,0,1]] -> 3
    [[1,1,1,1],[0,1,1,0]] -> 4
"""

def longest_line(mat):
    if not mat: return 0
    rows, cols = len(mat), len(mat[0])
    # dp[r][c][d] = length ending at (r,c) in direction d
    # d: 0=horiz, 1=vert, 2=diag, 3=anti-diag
    dp = [[[0]*4 for _ in range(cols)] for _ in range(rows)]
    best = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1:
                dp[r][c][0] = (dp[r][c-1][0] if c>0 else 0) + 1
                dp[r][c][1] = (dp[r-1][c][1] if r>0 else 0) + 1
                dp[r][c][2] = (dp[r-1][c-1][2] if r>0 and c>0 else 0) + 1
                dp[r][c][3] = (dp[r-1][c+1][3] if r>0 and c<cols-1 else 0) + 1
                best = max(best, max(dp[r][c]))
    return best

if __name__ == "__main__":
    print(longest_line([[0,1,1,0],[0,1,1,0],[0,0,0,1]]))  # 3
    print(longest_line([[1,1,1,1],[0,1,1,0]]))             # 4
