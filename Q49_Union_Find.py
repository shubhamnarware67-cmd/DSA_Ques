"""
Q49: Union-Find (Disjoint Set Union)
=====================================
Problem: Implement Union-Find data structure with path compression
and union by rank. Used for detecting cycles and connected components.

Example:
    Find if nodes 0 and 3 are connected after unions.
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1); uf.union(1, 2); uf.union(3, 4)
    print(uf.connected(0, 2))  # True
    print(uf.connected(0, 3))  # False
    print("Components:", uf.components)  # 2
