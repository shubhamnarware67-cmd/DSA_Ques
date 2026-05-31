"""
Q223: Redundant Connection (Union-Find)
=========================================
Problem: Given tree with one extra edge, find and return that edge
which, if removed, makes the graph a tree.

Example:
    [[1,2],[1,3],[2,3]] -> [2,3]
    [[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4]
"""

def find_redundant_connection(edges):
    parent = list(range(len(edges) + 1))
    rank = [0] * (len(edges) + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return False
        if rank[px] < rank[py]: px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]: rank[px] += 1
        return True

    for u, v in edges:
        if not union(u, v):
            return [u, v]

if __name__ == "__main__":
    print(find_redundant_connection([[1,2],[1,3],[2,3]]))         # [2,3]
    print(find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # [1,4]
