"""
Q453: All Ancestors of a Node in a DAG (Topological Sort)
============================================================
Problem: Given DAG, find all ancestors of each node (sorted).

Example:
    n=8, edges=[[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    -> ancestors of 5 = [0,3], etc.
"""
from collections import defaultdict, deque

def get_ancestors(n, edges):
    graph = defaultdict(list)
    in_degree = [0]*n
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    ancestors = [set() for _ in range(n)]
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []
    temp_indeg = in_degree[:]
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            temp_indeg[v] -= 1
            if temp_indeg[v] == 0:
                queue.append(v)

    for u in order:
        for v in graph[u]:
            ancestors[v].add(u)
            ancestors[v] |= ancestors[u]

    return [sorted(ancestors[i]) for i in range(n)]

if __name__ == "__main__":
    edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    result = get_ancestors(8, edges)
    for i, a in enumerate(result):
        print(i, a)
