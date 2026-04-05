"""
Q11: Binary Tree Level Order Traversal (BFS)
============================================
Problem: Given the root of a binary tree, return the level order traversal
of its nodes' values (i.e., from left to right, level by level).

Example:
    Input:  3
           / \
          9  20
            /  \
           15   7
    Output: [[3],[9,20],[15,7]]
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(level_order(root))  # [[3],[9,20],[15,7]]
