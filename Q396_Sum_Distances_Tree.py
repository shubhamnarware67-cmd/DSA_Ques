"""
Q396: Sum of Distances in Tree (Two-Pass DFS)
==============================================
Problem: Undirected tree of n nodes. For each node return sum of
distances to all other nodes.

Example:
    n=6, edges=[[0,1],[0,2],[2,3],[2,4],[2,5]] -> [8,12,6,10,10,10]
"""
from collections import defaultdict

def sum_of_distances_in_tree(n, edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v); graph[v].add(u)

    count = [1] * n   # Subtree size
    ans = [0] * n

    def dfs1(node, parent):
        for child in graph[node]:
            if child != parent:
                dfs1(child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

    def dfs2(node, parent):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + (n - count[child])
                dfs2(child, node)

    dfs1(0, -1)
    dfs2(0, -1)
    return ans

if __name__ == "__main__":
    print(sum_of_distances_in_tree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    # [8,12,6,10,10,10]
    print(sum_of_distances_in_tree(1, []))  # [0]
