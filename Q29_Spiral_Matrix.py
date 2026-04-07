"""
Q29: Spiral Matrix
==================
Problem: Given an m x n matrix, return all elements in spiral order.

Example:
    Input:  [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]
"""

def spiral_order(matrix):
    result = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):   result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):   result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1): result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1): result.append(matrix[r][left])
            left += 1
    return result

if __name__ == "__main__":
    print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
