"""
Q355: Range Sum Query 2D - Immutable (2D Prefix Sum)
=====================================================
Problem: Given 2D matrix, handle multiple sumRegion queries efficiently.
sumRegion(r1,c1,r2,c2) = sum of elements in sub-rectangle.

Example:
    matrix=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    sumRegion(2,1,4,3) -> 8
    sumRegion(1,1,2,2) -> 11
"""

class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0]*(n+1) for _ in range(m+1)]
        for r in range(m):
            for c in range(n):
                self.prefix[r+1][c+1] = (matrix[r][c] + self.prefix[r][c+1] +
                                          self.prefix[r+1][c] - self.prefix[r][c])

    def sumRegion(self, r1, c1, r2, c2):
        p = self.prefix
        return p[r2+1][c2+1] - p[r1][c2+1] - p[r2+1][c1] + p[r1][c1]

if __name__ == "__main__":
    nm = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
    print(nm.sumRegion(2,1,4,3))  # 8
    print(nm.sumRegion(1,1,2,2))  # 11
    print(nm.sumRegion(1,2,2,4))  # 12
