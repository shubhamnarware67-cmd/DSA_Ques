"""
Q398: Reorder Routes to Make All Paths Lead to City Zero (BFS)
==============================================================
Problem: n cities connected in a tree via directed edges. Reorder minimum
edges so all cities can reach city 0.

Example:
    n=6, connections=[[0,1],[1,3],[2,3],[4,0],[4,5]] -> 3
    n=5, connections=[[1,0],[1,2],[3,2],[3,4]]        -> 2
"""
from collections import defaultdict, deque

def min_reorder(n, connections):
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append((v, 1))   # Original direction (needs flip)
        graph[v].append((u, 0))   # Reverse direction (already correct)

    visited = {0}
    queue = deque([0])
    changes = 0
    while queue:
        node = queue.popleft()
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                changes += cost
                queue.append(neighbor)
    return changes

if __name__ == "__main__":
    print(min_reorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))  # 3
    print(min_reorder(5, [[1,0],[1,2],[3,2],[3,4]]))         # 2
