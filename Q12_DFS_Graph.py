"""
Q12: Depth First Search (DFS) in Graph
=======================================
Problem: Given a graph (adjacency list) and a start node,
perform DFS and return the visited order.

Example:
    graph = {0:[1,2], 1:[0,3], 2:[0,4], 3:[1], 4:[2]}
    start = 0
    Output: [0, 1, 3, 2, 4]
"""

def dfs(graph, start):
    visited = []
    stack = [start]
    seen = set()
    while stack:
        node = stack.pop()
        if node not in seen:
            seen.add(node)
            visited.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in seen:
                    stack.append(neighbor)
    return visited

def dfs_recursive(graph, node, seen=None, visited=None):
    if seen is None: seen = set()
    if visited is None: visited = []
    seen.add(node)
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in seen:
            dfs_recursive(graph, neighbor, seen, visited)
    return visited

if __name__ == "__main__":
    graph = {0:[1,2], 1:[0,3], 2:[0,4], 3:[1], 4:[2]}
    print(dfs(graph, 0))            # [0, 1, 3, 2, 4]
    print(dfs_recursive(graph, 0))  # [0, 1, 3, 2, 4]
