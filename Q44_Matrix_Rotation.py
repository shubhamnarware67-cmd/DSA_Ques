"""
Q44: Rotate Image (Matrix 90 degrees)
======================================
Problem: Given an n x n 2D matrix, rotate it 90 degrees clockwise in-place.

Example:
    Input:  [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate(matrix):
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    for row in matrix:
        print(row)
    # [7,4,1]
    # [8,5,2]
    # [9,6,3]
