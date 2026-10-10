"""
Q448: Count Square Submatrices with All Ones (DP)
=====================================================
Problem: Given binary matrix, count number of square submatrices with all 1s.

Example:
    [[0,1,1,1],[1,1,1,1],[0,1,1,1]] -> 15
    [[1,0,1],[1,1,0],[1,1,0]] -> 7
"""

def count_squares(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0]*n for _ in range(m)]
    total = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                total += dp[i][j]
    return total

if __name__ == "__main__":
    print(count_squares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))  # 15
    print(count_squares([[1,0,1],[1,1,0],[1,1,0]]))         # 7
