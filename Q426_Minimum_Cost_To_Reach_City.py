"""
Q426: Minimum Cost to Reach City With Discounts (Modified Dijkstra)
======================================================================
Problem: Roads have costs. You have 'discounts' which halve a road's cost
(rounded up), used at most once per road. Find min cost path 0 to n-1.

Example:
    n=5, highways=[[0,1,4],[1,2,6],[2,3,3]], discounts=2 -> 9
"""
import heapq
from collections import defaultdict

def minimum_cost(n, highways, discounts):
    graph = defaultdict(list)
    for u, v, w in highways:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # State: (cost, node, discounts_used)
    dist = [[float('inf')] * (discounts+1) for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        cost, u, used = heapq.heappop(heap)
        if cost > dist[u][used]: continue
        for v, w in graph[u]:
            # Without discount
            if cost + w < dist[v][used]:
                dist[v][used] = cost + w
                heapq.heappush(heap, (cost+w, v, used))
            # With discount
            if used < discounts:
                discounted = cost + (w+1)//2
                if discounted < dist[v][used+1]:
                    dist[v][used+1] = discounted
                    heapq.heappush(heap, (discounted, v, used+1))

    result = min(dist[n-1])
    return result if result != float('inf') else -1

if __name__ == "__main__":
    print(minimum_cost(5, [[0,1,4],[1,2,6],[2,3,3]], 2))  # likely connects partially
