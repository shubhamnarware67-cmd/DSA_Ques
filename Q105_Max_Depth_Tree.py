"""
Q105: Maximum Depth of Binary Tree
====================================
Problem: Given root of binary tree, return its maximum depth
(number of nodes along the longest path from root to leaf).

Example:
    [3,9,20,null,null,15,7] -> 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# BFS approach
from collections import deque
def max_depth_bfs(root):
    if not root: return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return depth

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))      # 3
    print(max_depth_bfs(root))  # 3
