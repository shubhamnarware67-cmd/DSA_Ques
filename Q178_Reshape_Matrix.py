"""
Q178: Reshape the Matrix
==========================
Problem: Given m x n matrix and integers r and c, return the reshaped
matrix. If not possible, return original matrix.

Example:
    mat=[[1,2],[3,4]], r=1, c=4 -> [[1,2,3,4]]
    mat=[[1,2],[3,4]], r=2, c=4 -> [[1,2],[3,4]] (not possible)
"""

def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    flat = [mat[i][j] for i in range(m) for j in range(n)]
    return [[flat[i*c+j] for j in range(c)] for i in range(r)]

if __name__ == "__main__":
    print(matrix_reshape([[1,2],[3,4]], 1, 4))  # [[1,2,3,4]]
    print(matrix_reshape([[1,2],[3,4]], 2, 4))  # [[1,2],[3,4]]
