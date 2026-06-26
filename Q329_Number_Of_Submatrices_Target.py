"""
Q329: Number of Submatrices That Sum to Target (Prefix Sum)
============================================================
Problem: Count number of non-empty submatrices with sum equal to target.

Example:
    matrix=[[0,1,0],[1,1,1],[0,1,0]], target=0 -> 4
    matrix=[[1,-1],[-1,1]], target=0 -> 5
"""
from collections import defaultdict

def num_submatrix_sum_target(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(1, cols):
            matrix[r][c] += matrix[r][c-1]

    count = 0
    for c1 in range(cols):
        for c2 in range(c1, cols):
            seen = defaultdict(int)
            seen[0] = 1
            total = 0
            for r in range(rows):
                total += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                count += seen[total - target]
                seen[total] += 1
    return count

if __name__ == "__main__":
    print(num_submatrix_sum_target([[0,1,0],[1,1,1],[0,1,0]], 0))  # 4
    print(num_submatrix_sum_target([[1,-1],[-1,1]], 0))             # 5
