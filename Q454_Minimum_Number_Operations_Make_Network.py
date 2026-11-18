"""
Q454: Number of Operations to Make Network Connected (Union-Find)
=====================================================================
Problem: n computers, connections (cables). Find min operations to connect
all computers (move 1 cable per operation). Return -1 if impossible.

Example:
    n=4, connections=[[0,1],[0,2],[1,2]] -> 1
    n=6, connections=[[0,1],[0,2],[0,3],[1,2],[1,3]] -> 2
    n=6, connections=[[0,1],[0,2],[0,3],[1,2]] -> -1
"""

def make_connected(n, connections):
    if len(connections) < n - 1: return -1
    parent = list(range(n))
    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        px, py = find(x), find(y)
        if px != py: parent[px] = py; return True
        return False

    components = n
    for u, v in connections:
        if union(u, v): components -= 1
    return components - 1

if __name__ == "__main__":
    print(make_connected(4, [[0,1],[0,2],[1,2]]))             # 1
    print(make_connected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]])) # 2
    print(make_connected(6, [[0,1],[0,2],[0,3],[1,2]]))        # -1
