"""
Q219: Longest Path in a Directed Acyclic Graph (DAG)
======================================================
Problem: Find the longest path in a DAG using topological sort + DP.

Example:
    V=6, edges=[(0,1,5),(0,2,3),(1,3,6),(1,2,2),(2,4,4),(2,3,7),(3,5,1),(4,5,4),(5,None,0)]
    Longest path from 0 = 11 (0->2->3->5)
"""
from collections import defaultdict, deque

def longest_path_dag(V, edges):
    graph = defaultdict(list)
    in_degree = [0] * V
    for u, v, w in edges:
        graph[u].append((v, w))
        in_degree[v] += 1
    # Topological sort
    queue = deque([i for i in range(V) if in_degree[i] == 0])
    dist = [0] * V
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            dist[v] = max(dist[v], dist[u] + w)
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return max(dist)

if __name__ == "__main__":
    edges = [(0,1,5),(0,2,3),(1,3,6),(1,2,2),(2,4,4),(2,3,7),(3,5,1),(4,5,4)]
    print(f"Longest path: {longest_path_dag(6, edges)}")  # 11
