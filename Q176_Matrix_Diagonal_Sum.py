"""
Q176: Matrix Diagonal Sum
==========================
Problem: Given square matrix, return sum of elements on both primary
and secondary diagonals. Count center element only once (odd n).

Example:
    [[1,2,3],[4,5,6],[7,8,9]] -> 25
    [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] -> 8
"""

def diagonal_sum(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]          # Primary diagonal
        total += mat[i][n-1-i]      # Secondary diagonal
    if n % 2 == 1:
        total -= mat[n//2][n//2]    # Remove double-counted center
    return total

if __name__ == "__main__":
    print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))   # 25
    print(diagonal_sum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))  # 8
