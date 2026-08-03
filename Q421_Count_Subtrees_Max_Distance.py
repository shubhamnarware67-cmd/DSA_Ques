"""
Q421: Count Subtrees With Max Distance Between Cities (Bitmask + BFS)
========================================================================
Problem: Tree with n nodes. For each d in [1,n-1], count subtrees where
max distance between any two nodes equals d.

Example:
    n=4, edges=[[1,2],[2,3],[2,4]] -> [3,4,0]
    n=2, edges=[[1,2]] -> [1]
"""
from collections import defaultdict

def count_subgraphs_for_each_diameter(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    result = [0] * (n-1)

    for mask in range(1, 1 << n):
        nodes = [i for i in range(n) if mask & (1 << i)]
        if len(nodes) < 2: continue
        # Check if subset forms connected subtree using only edges within subset
        visited = set()
        stack = [nodes[0]]
        edge_count = 0
        while stack:
            node = stack.pop()
            if node in visited: continue
            visited.add(node)
            for neighbor in graph[node]:
                if mask & (1 << neighbor):
                    edge_count += 1
                    if neighbor not in visited:
                        stack.append(neighbor)
        if visited != set(nodes): continue
        if edge_count // 2 != len(nodes) - 1: continue  # Must be tree (no extra edges)

        # BFS to find diameter
        def bfs(start):
            dist = {start: 0}
            queue = [start]
            farthest, max_d = start, 0
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if mask & (1 << neighbor) and neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        if dist[neighbor] > max_d:
                            max_d = dist[neighbor]; farthest = neighbor
                        queue.append(neighbor)
            return farthest, max_d

        u, _ = bfs(nodes[0])
        _, diameter = bfs(u)
        if diameter > 0:
            result[diameter-1] += 1

    return result

if __name__ == "__main__":
    print(count_subgraphs_for_each_diameter(4, [[1,2],[2,3],[2,4]]))  # [3,4,0]
    print(count_subgraphs_for_each_diameter(2, [[1,2]]))               # [1]
