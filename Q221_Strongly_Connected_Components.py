"""
Q221: Strongly Connected Components (Kosaraju's Algorithm)
===========================================================
Problem: Find all SCCs in a directed graph. An SCC is a maximal set
where every vertex is reachable from every other vertex.

Example:
    graph = {0:[2,3],1:[0],2:[1],3:[4],4:[]}
    SCCs: [[0,1,2],[3],[4]]
"""
from collections import defaultdict

def kosaraju(n, adj):
    visited = [False] * n
    finish_stack = []

    def dfs1(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]: dfs1(u)
        finish_stack.append(v)

    for i in range(n):
        if not visited[i]: dfs1(i)

    radj = defaultdict(list)
    for v in adj:
        for u in adj[v]: radj[u].append(v)

    visited = [False] * n
    sccs = []

    def dfs2(v, comp):
        visited[v] = True
        comp.append(v)
        for u in radj[v]:
            if not visited[u]: dfs2(u, comp)

    while finish_stack:
        v = finish_stack.pop()
        if not visited[v]:
            comp = []
            dfs2(v, comp)
            sccs.append(sorted(comp))
    return sccs

if __name__ == "__main__":
    adj = {0:[2,3],1:[0],2:[1],3:[4],4:[]}
    print(kosaraju(5, adj))  # [[0,1,2],[3],[4]] (order may vary)
