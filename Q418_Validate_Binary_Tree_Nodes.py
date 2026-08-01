"""
Q418: Validate Binary Tree Nodes
===================================
Problem: Given n nodes with leftChild[i], rightChild[i] arrays, validate
if they form exactly one valid binary tree.

Example:
    n=4, leftChild=[1,-1,3,-1], rightChild=[2,-1,-1,-1] -> True
    n=4, leftChild=[1,-1,3,-1], rightChild=[2,3,-1,-1]   -> False (node 3 has 2 parents)
"""

def validate_binary_tree_nodes(n, leftChild, rightChild):
    indegree = [0] * n
    for l in leftChild:
        if l != -1: indegree[l] += 1
    for r in rightChild:
        if r != -1: indegree[r] += 1
    if any(d > 1 for d in indegree): return False

    roots = [i for i in range(n) if indegree[i] == 0]
    if len(roots) != 1: return False

    visited = set()
    stack = [roots[0]]
    while stack:
        node = stack.pop()
        if node in visited: return False
        visited.add(node)
        if leftChild[node] != -1: stack.append(leftChild[node])
        if rightChild[node] != -1: stack.append(rightChild[node])
    return len(visited) == n

if __name__ == "__main__":
    print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,-1,-1,-1]))  # True
    print(validate_binary_tree_nodes(4, [1,-1,3,-1], [2,3,-1,-1]))   # False
