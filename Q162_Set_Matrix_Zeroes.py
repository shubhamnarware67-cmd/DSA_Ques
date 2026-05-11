"""
Q162: Set Matrix Zeroes
========================
Problem: If an element is 0, set its entire row and column to 0. In-place.
Use O(1) extra space.

Example:
    [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]
"""

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row_zero:
        for j in range(cols): matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows): matrix[i][0] = 0

if __name__ == "__main__":
    m = [[1,1,1],[1,0,1],[1,1,1]]
    set_zeroes(m)
    for row in m: print(row)
    # [1,0,1], [0,0,0], [1,0,1]
