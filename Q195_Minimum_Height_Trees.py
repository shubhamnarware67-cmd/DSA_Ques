"""
Q195: Minimum Height Trees
============================
Problem: A tree can be rooted at any node. Find all nodes that minimize
the tree height (roots of minimum height trees).

Example:
    n=4, edges=[[1,0],[1,2],[1,3]] -> [1]
    n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]] -> [3,4]
"""
from collections import deque

def find_min_height_trees(n, edges):
    if n == 1: return [0]
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    leaves = deque([i for i in range(n) if len(adj[i]) == 1])
    remaining = n
    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = deque()
        while leaves:
            leaf = leaves.popleft()
            neighbor = adj[leaf].pop()
            adj[neighbor].remove(leaf)
            if len(adj[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves
    return list(leaves)

if __name__ == "__main__":
    print(find_min_height_trees(4, [[1,0],[1,2],[1,3]]))          # [1]
    print(find_min_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))  # [3,4]
