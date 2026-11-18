"""
Q455: Find Eventual Safe States (DFS + Coloring)
====================================================
Problem: Directed graph. A node is "safe" if every path from it leads to
a terminal node (no cycles). Return all safe nodes sorted.

Example:
    graph=[[1,2],[2,3],[5],[0],[5],[],[]] -> [2,4,5,6]
"""

def eventual_safe_nodes(graph):
    n = len(graph)
    color = [0] * n  # 0=unvisited, 1=visiting, 2=safe

    def dfs(node):
        if color[node] != 0:
            return color[node] == 2
        color[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        color[node] = 2
        return True

    return [i for i in range(n) if dfs(i)]

if __name__ == "__main__":
    print(eventual_safe_nodes([[1,2],[2,3],[5],[0],[5],[],[]]))  # [2,4,5,6]
    print(eventual_safe_nodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))  # [4]
