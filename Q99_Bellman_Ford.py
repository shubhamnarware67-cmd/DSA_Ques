"""
Q99: Bellman-Ford Algorithm (Shortest Path with Negative Weights)
==================================================================
Problem: Find shortest paths from a source to all vertices in a
weighted graph. Handles negative weight edges (unlike Dijkstra).
Detects negative weight cycles.

Example:
    V=5, edges=[(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)]
    Source=0 -> dist=[0,-1,2,-2,1]
"""

def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # Check for negative weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("Negative weight cycle detected!")
            return None
    return dist

if __name__ == "__main__":
    edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),
             (3,2,5),(3,1,1),(4,3,-3)]
    print(bellman_ford(5, edges, 0))  # [0,-1,2,-2,1]
