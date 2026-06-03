"""
Q238: Sparse Table (Range Minimum Query)
==========================================
Problem: Build a Sparse Table for O(1) range minimum query after O(n log n)
preprocessing. Ideal for static arrays.

Example:
    arr=[2,4,3,1,6,7,8,9,1,7]
    RMQ(0,4) -> 1 (min of [2,4,3,1,6])
    RMQ(4,9) -> 1 (min of [6,7,8,9,1,7])
"""
import math

class SparseTable:
    def __init__(self, arr):
        n = len(arr)
        k = int(math.log2(n)) + 1 if n > 0 else 1
        self.table = [[float('inf')]*n for _ in range(k)]
        self.log2 = [0] * (n+1)
        for i in range(2, n+1):
            self.log2[i] = self.log2[i//2] + 1
        self.table[0] = arr[:]
        for j in range(1, k):
            for i in range(n - (1 << j) + 1):
                self.table[j][i] = min(self.table[j-1][i],
                                       self.table[j-1][i + (1 << (j-1))])

    def query(self, l, r):
        length = r - l + 1
        k = self.log2[length]
        return min(self.table[k][l], self.table[k][r - (1 << k) + 1])

if __name__ == "__main__":
    arr = [2,4,3,1,6,7,8,9,1,7]
    st = SparseTable(arr)
    print(st.query(0,4))  # 1
    print(st.query(4,9))  # 1
    print(st.query(0,2))  # 2
