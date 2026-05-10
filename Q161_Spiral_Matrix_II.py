"""
Q161: Spiral Matrix II (Generate)
===================================
Problem: Given positive integer n, generate an n x n matrix
filled with elements from 1 to n^2 in spiral order.

Example:
    n=3 -> [[1,2,3],[8,9,4],[7,6,5]]
    n=1 -> [[1]]
"""

def generate_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    while top <= bottom and left <= right:
        for c in range(left, right+1):   matrix[top][c] = num; num+=1
        top += 1
        for r in range(top, bottom+1):   matrix[r][right] = num; num+=1
        right -= 1
        for c in range(right, left-1,-1):matrix[bottom][c] = num; num+=1
        bottom -= 1
        for r in range(bottom, top-1,-1):matrix[r][left] = num; num+=1
        left += 1
    return matrix

if __name__ == "__main__":
    for row in generate_matrix(3): print(row)
    # [1,2,3]
    # [8,9,4]
    # [7,6,5]
