"""
Q41: Dijkstra's Shortest Path Algorithm
========================================
Problem: Given a weighted graph and a source node,
find shortest distances from source to all other nodes.

Example:
    graph = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2),(3,5)], 3:[]}
    Source: 0
    Output: {0:0, 1:3, 2:1, 3:4}
"""
import heapq

def dijkstra(graph, src):
    dist = {node: float('inf') for node in graph}
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

if __name__ == "__main__":
    graph = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2),(3,5)], 3:[]}
    print(dijkstra(graph, 0))  # {0:0, 1:3, 2:1, 3:4}
