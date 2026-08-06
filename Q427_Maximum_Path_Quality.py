"""
Q427: Maximum Path Quality of a Graph (DFS + Backtracking)
=============================================================
Problem: Graph with values[i] and time costs on edges. Find max sum of
values visiting nodes (can revisit) within maxTime, must return to node 0.

Example:
    values=[0,32,10,43], edges=[[0,1,10],[1,2,15],[0,3,10]], maxTime=49 -> 75
"""
from collections import defaultdict

def maximal_path_quality(values, edges, maxTime):
    graph = defaultdict(list)
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))

    n = len(values)
    visited = [False] * n
    visited[0] = True
    best = [0]

    def dfs(node, time_left, quality):
        if node == 0:
            best[0] = max(best[0], quality)
        for neighbor, t in graph[node]:
            if t <= time_left:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor, time_left - t, quality + values[neighbor])
                    visited[neighbor] = False
                else:
                    dfs(neighbor, time_left - t, quality)

    dfs(0, maxTime, values[0])
    return best[0]

if __name__ == "__main__":
    values = [0,32,10,43]
    edges = [[0,1,10],[1,2,15],[0,3,10]]
    print(maximal_path_quality(values, edges, 49))  # 75
