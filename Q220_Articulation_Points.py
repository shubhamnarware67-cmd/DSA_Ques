"""
Q220: Articulation Points (Bridge Finding) in Graph
=====================================================
Problem: Find all articulation points — vertices whose removal increases
the number of connected components. Uses DFS + low values.

Example:
    graph = {0:[1,2],1:[0,2],2:[0,1,3],3:[2,4,5],4:[3],5:[3]}
    Articulation points: [2, 3]
"""

def find_articulation_points(graph, n):
    visited = [False] * n
    disc = [0] * n
    low = [0] * n
    parent = [-1] * n
    ap = [False] * n
    timer = [0]

    def dfs(u):
        children = 0
        visited[u] = True
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1: ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]: ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]: dfs(i)
    return [i for i in range(n) if ap[i]]

if __name__ == "__main__":
    graph = {0:[1,2],1:[0,2],2:[0,1,3],3:[2,4,5],4:[3],5:[3]}
    print(find_articulation_points(graph, 6))  # [2, 3]
