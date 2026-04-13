"""
Q42: Topological Sort (Kahn's Algorithm - BFS)
===============================================
Problem: Given a Directed Acyclic Graph (DAG), return a topological ordering.
(Used in course scheduling, build systems, etc.)

Example:
    5 courses, prerequisites: [[1,0],[2,0],[3,1],[4,3]]
    Output: [0, 2, 1, 3, 4]
"""
from collections import deque

def topological_sort(num_nodes, edges):
    graph = [[] for _ in range(num_nodes)]
    in_degree = [0] * num_nodes
    for u, v in edges:
        graph[v].append(u)
        in_degree[u] += 1
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_nodes else []  # [] means cycle

if __name__ == "__main__":
    print(topological_sort(5, [[1,0],[2,0],[3,1],[4,3]]))  # [0,2,1,3,4] or similar
