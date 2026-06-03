"""
Q237: Fenwick Tree (Binary Indexed Tree)
==========================================
Problem: Build a BIT supporting:
- Prefix sum query in O(log n)
- Point update in O(log n)
Simpler than Segment Tree with same complexity.

Example:
    arr=[1,3,5,7,9,11]
    prefix_sum(4) -> 16 (1+3+5+7)
    update(3, +2) (add 2 to index 3)
    prefix_sum(4) -> 18
"""

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)

    def update(self, i, delta):
        i += 1  # 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Next node

    def prefix_sum(self, i):
        i += 1  # 1-indexed
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # Parent node
        return total

    def range_sum(self, l, r):
        return self.prefix_sum(r) - (self.prefix_sum(l-1) if l > 0 else 0)

    @classmethod
    def from_array(cls, arr):
        bt = cls(len(arr))
        for i, val in enumerate(arr):
            bt.update(i, val)
        return bt

if __name__ == "__main__":
    bt = FenwickTree.from_array([1,3,5,7,9,11])
    print(bt.prefix_sum(3))   # 16 (1+3+5+7)
    bt.update(3, 2)            # Add 2 to index 3
    print(bt.prefix_sum(3))   # 18
    print(bt.range_sum(2,4))  # 7+9 = 16
