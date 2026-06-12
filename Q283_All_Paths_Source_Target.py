"""
Q283: All Paths From Source to Target (DFS)
=============================================
Problem: Given DAG with n nodes, return all paths from node 0 to node n-1.

Example:
    [[1,2],[3],[3],[]] -> [[0,1,3],[0,2,3]]
    [[4,3,1],[3,2,4],[3],[4],[]] -> [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

def all_paths_source_target(graph):
    result = []
    def dfs(node, path):
        if node == len(graph)-1:
            result.append(list(path)); return
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()
    dfs(0, [0])
    return result

if __name__ == "__main__":
    print(all_paths_source_target([[1,2],[3],[3],[]]))
    # [[0,1,3],[0,2,3]]
    print(all_paths_source_target([[4,3,1],[3,2,4],[3],[4],[]]))
    # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
