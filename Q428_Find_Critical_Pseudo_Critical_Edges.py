"""
Q428: Find Critical and Pseudo-Critical Edges in MST
========================================================
Problem: Find critical edges (removing increases MST weight or disconnects)
and pseudo-critical edges (can be in some MST).

Example:
    n=5, edges=[[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    -> [[0,1],[2,3,4,5]]
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.components = n
    def find(self, x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]: self.rank[px] += 1
        self.components -= 1
        return True

def find_critical_pseudo_edges(n, edges):
    indexed = [(w,u,v,i) for i,(u,v,w) in enumerate(edges)]
    indexed.sort()

    def mst_weight(skip=-1, force=None):
        uf = UnionFind(n)
        weight = 0
        if force:
            w,u,v,_ = force
            uf.union(u,v); weight += w
        for w,u,v,i in indexed:
            if i == skip: continue
            if uf.union(u,v): weight += w
        return weight if uf.components == 1 else float('inf')

    base = mst_weight()
    critical, pseudo = [], []
    for w,u,v,i in indexed:
        if mst_weight(skip=i) > base:
            critical.append(i)
        elif mst_weight(force=(w,u,v,i)) == base:
            pseudo.append(i)
    return [critical, pseudo]

if __name__ == "__main__":
    edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
    print(find_critical_pseudo_edges(5, edges))
    # [[0,1],[2,3,4,5]]
