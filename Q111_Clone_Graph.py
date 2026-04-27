"""
Q111: Clone Graph
==================
Problem: Given a reference to a node in a connected undirected graph,
return a deep copy (clone) of the graph.

Example:
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: Deep copy with same structure
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

def clone_graph(node):
    if not node: return None
    cloned = {}
    def dfs(n):
        if n in cloned: return cloned[n]
        clone = Node(n.val)
        cloned[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)

if __name__ == "__main__":
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    cloned = clone_graph(n1)
    print(cloned.val, [n.val for n in cloned.neighbors])  # 1 [2, 4]
    print(cloned is not n1)  # True (different object)
