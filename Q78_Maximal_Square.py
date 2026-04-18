"""
Q78: Maximal Square (DP)
==========================
Problem: Given a binary matrix, find the largest square containing
only 1s and return its area.

Example:
    [["1","0","1","0","0"],
     ["1","0","1","1","1"],
     ["1","1","1","1","1"],
     ["1","0","0","1","0"]]
    Output: 4 (2x2 square)
"""

def maximal_square(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    max_side = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side * max_side

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
              ["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximal_square(matrix))  # 4
