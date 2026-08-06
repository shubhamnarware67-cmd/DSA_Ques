"""
Q425: Number of Ways to Arrive at Destination (Dijkstra + DP)
================================================================
Problem: Find number of shortest paths from node 0 to node n-1.
Mod 10^9+7.

Example:
    n=7, roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],
                [6,5,1],[2,5,1],[0,4,5],[4,6,2]] -> 4
"""
import heapq
from collections import defaultdict

def count_paths(n, roads):
    MOD = 10**9 + 7
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    heap = [(0, 0)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                ways[v] = ways[u]
                heapq.heappush(heap, (dist[v], v))
            elif dist[u] + w == dist[v]:
                ways[v] = (ways[v] + ways[u]) % MOD

    return ways[n-1]

if __name__ == "__main__":
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],
             [6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    print(count_paths(7, roads))  # 4
