"""
Q298: Maximum Width of Binary Tree
=====================================
Problem: Return maximum width of binary tree (max number of nodes between
leftmost and rightmost node at any level, including nulls between).

Example:
    [1,3,2,5,3,null,9]    -> 4
    [1,3,2,5,null,null,9,6,null,7] -> 7
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def width_of_binary_tree(root):
    if not root: return 0
    max_width = 0
    queue = deque([(root, 0)])
    while queue:
        level_len = len(queue)
        _, first_idx = queue[0]
        for _ in range(level_len):
            node, idx = queue.popleft()
            idx -= first_idx  # Normalize to avoid overflow
            if node.left:  queue.append((node.left,  2*idx))
            if node.right: queue.append((node.right, 2*idx+1))
        max_width = max(max_width, idx + 1)
    return max_width

if __name__ == "__main__":
    root = TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)),TreeNode(2,None,TreeNode(9)))
    print(width_of_binary_tree(root))  # 4
