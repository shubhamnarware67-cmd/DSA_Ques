"""
Q216: Kruskal's Minimum Spanning Tree
=======================================
Problem: Find minimum spanning tree of a weighted undirected graph
using Kruskal's algorithm (greedy + union-find).

Example:
    V=4, edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    MST cost = 19  (edges: 2-3, 0-3, 0-1)
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        return True

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(V)
    mst_cost = 0
    mst_edges = []
    for u, v, w in edges:
        if uf.union(u, v):
            mst_cost += w
            mst_edges.append((u, v, w))
    return mst_cost, mst_edges

if __name__ == "__main__":
    edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    cost, tree = kruskal(4, edges)
    print(f"MST Cost: {cost}")    # 19
    print(f"MST Edges: {tree}")   # [(2,3,4),(0,3,5),(0,1,10)]
