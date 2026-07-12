"""
Q397: Count Unreachable Pairs of Nodes in an Undirected Graph
==============================================================
Problem: Count pairs of nodes that cannot reach each other.

Example:
    n=3, edges=[[0,1],[0,2],[1,2]] -> 0
    n=7, edges=[[0,2],[0,5],[2,4],[1,6],[5,4]] -> 14
"""

def count_pairs(n, edges):
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return
        if size[px] < size[py]: px, py = py, px
        parent[py] = px; size[px] += size[py]

    for u, v in edges:
        union(u, v)

    from collections import Counter
    comp_sizes = Counter(find(i) for i in range(n))
    result = 0
    remaining = n
    for sz in comp_sizes.values():
        remaining -= sz
        result += sz * remaining
    return result

if __name__ == "__main__":
    print(count_pairs(3, [[0,1],[0,2],[1,2]]))          # 0
    print(count_pairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]])) # 14
