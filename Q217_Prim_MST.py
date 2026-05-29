"""
Q217: Prim's Minimum Spanning Tree
=====================================
Problem: Find MST using Prim's algorithm (greedy + min heap).
Start from vertex 0 and greedily pick the minimum edge crossing the cut.

Example:
    graph = {0:[(1,2),(3,6)], 1:[(0,2),(2,3),(3,8),(4,5)],
             2:[(1,3),(4,7)], 3:[(0,6),(1,8),(4,9)], 4:[(1,5),(2,7),(3,9)]}
    MST cost = 16
"""
import heapq

def prim(graph, start=0):
    visited = set()
    heap = [(0, start, -1)]  # (weight, node, from)
    mst_cost = 0
    mst_edges = []
    while heap:
        w, u, prev = heapq.heappop(heap)
        if u in visited: continue
        visited.add(u)
        mst_cost += w
        if prev != -1: mst_edges.append((prev, u, w))
        for v, weight in graph.get(u, []):
            if v not in visited:
                heapq.heappush(heap, (weight, v, u))
    return mst_cost, mst_edges

if __name__ == "__main__":
    graph = {0:[(1,2),(3,6)], 1:[(0,2),(2,3),(3,8),(4,5)],
             2:[(1,3),(4,7)], 3:[(0,6),(1,8),(4,9)], 4:[(1,5),(2,7),(3,9)]}
    cost, edges = prim(graph)
    print(f"MST Cost: {cost}")   # 16
    print(f"MST Edges: {edges}")
