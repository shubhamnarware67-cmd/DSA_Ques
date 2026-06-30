"""
Q354: Matrix Block Sum (2D Prefix Sum)
=======================================
Problem: Given matrix and k, compute answer where answer[i][j] =
sum of all elements mat[r][c] where i-k<=r<=i+k, j-k<=c<=j+k.

Example:
    mat=[[1,2,3],[4,5,6],[7,8,9]], k=1 -> [[12,21,16],[27,45,33],[24,39,28]]
"""

def matrix_block_sum(mat, k):
    m, n = len(mat), len(mat[0])
    prefix = [[0]*(n+1) for _ in range(m+1)]
    for r in range(m):
        for c in range(n):
            prefix[r+1][c+1] = (mat[r][c] + prefix[r][c+1] +
                                 prefix[r+1][c] - prefix[r][c])

    def query(r1, c1, r2, c2):
        r1, c1 = max(0,r1), max(0,c1)
        r2, c2 = min(m-1,r2), min(n-1,c2)
        return (prefix[r2+1][c2+1] - prefix[r1][c2+1] -
                prefix[r2+1][c1] + prefix[r1][c1])

    return [[query(i-k,j-k,i+k,j+k) for j in range(n)] for i in range(m)]

if __name__ == "__main__":
    for row in matrix_block_sum([[1,2,3],[4,5,6],[7,8,9]], 1):
        print(row)
    # [12,21,16], [27,45,33], [24,39,28]
