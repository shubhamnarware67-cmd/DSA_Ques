"""
Q300: All Nodes at Distance K in Binary Tree
===============================================
Problem: Return all nodes at distance k from target node in binary tree.

Example:
    root=[3,5,1,6,2,0,8,null,null,7,4], target=5, k=2
    -> [7,4,1]
"""
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def distance_k(root, target, k):
    # Build undirected graph
    graph = defaultdict(list)
    def build(node, parent):
        if not node: return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        build(node.left, node)
        build(node.right, node)
    build(root, None)

    # BFS from target
    visited = {target.val}
    queue = deque([(target.val, 0)])
    result = []
    while queue:
        node, dist = queue.popleft()
        if dist == k: result.append(node)
        if dist < k:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist+1))
    return result

if __name__ == "__main__":
    root = TreeNode(3,
                    TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),
                    TreeNode(1,TreeNode(0),TreeNode(8)))
    target = root.left  # node 5
    print(distance_k(root, target, 2))  # [7,4,1]
