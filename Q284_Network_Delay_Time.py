"""
Q284: Network Delay Time (Dijkstra)
=====================================
Problem: Network of n nodes with directed weighted edges (times).
Signal sent from node k. Find time for all nodes to receive signal.
Return -1 if impossible.

Example:
    times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2 -> 2
"""
import heapq
from collections import defaultdict

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n+1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1

if __name__ == "__main__":
    print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
    print(network_delay_time([[1,2,1]], 2, 1))                   # 1
    print(network_delay_time([[1,2,1]], 2, 2))                   # -1
