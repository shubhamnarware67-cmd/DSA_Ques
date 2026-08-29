"""
Q430: Reachable Nodes In Subdivided Graph (Dijkstra)
========================================================
Problem: Each edge subdivided into cnt[i] nodes. Find how many nodes
(original + subdivided) reachable within maxMoves from node 0.

Example:
    edges=[[0,1,10],[0,2,1],[1,2,2]], maxMoves=6, n=3 -> 13
"""
import heapq
from collections import defaultdict

def reachable_nodes(edges, maxMoves, n):
    graph = defaultdict(dict)
    for u, v, cnt in edges:
        graph[u][v] = cnt
        graph[v][u] = cnt

    dist = {0: 0}
    heap = [(0, 0)]
    visited_nodes = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited_nodes: continue
        visited_nodes.add(u)
        for v, cnt in graph[u].items():
            nd = d + cnt + 1
            if nd <= maxMoves and (v not in dist or nd < dist[v]):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    result = len(visited_nodes)
    for u, v, cnt in edges:
        a = max(0, maxMoves - dist.get(u, float('inf'))) if u in dist else 0
        b = max(0, maxMoves - dist.get(v, float('inf'))) if v in dist else 0
        result += min(cnt, a + b)
    return result

if __name__ == "__main__":
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    print(reachable_nodes(edges, 6, 3))  # 13
