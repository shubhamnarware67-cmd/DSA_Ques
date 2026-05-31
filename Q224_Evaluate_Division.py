"""
Q224: Evaluate Division (Graph + BFS)
=======================================
Problem: Given equations [A/B=val], answer queries [X/Y=?].
Return -1 if cannot be determined.

Example:
    equations=[["a","b"],["b","c"]], values=[2.0,3.0]
    queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    -> [6.0, 0.5, -1.0, 1.0, -1.0]
"""
from collections import defaultdict, deque

def calc_equation(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1/val

    def bfs(src, dst):
        if src not in graph or dst not in graph: return -1.0
        if src == dst: return 1.0
        visited = {src}
        queue = deque([(src, 1.0)])
        while queue:
            node, prod = queue.popleft()
            if node == dst: return prod
            for neighbor, val in graph[node].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, prod*val))
        return -1.0

    return [bfs(s, t) for s, t in queries]

if __name__ == "__main__":
    eqs = [["a","b"],["b","c"]]
    vals = [2.0, 3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(calc_equation(eqs, vals, queries))  # [6.0,0.5,-1.0,1.0,-1.0]
