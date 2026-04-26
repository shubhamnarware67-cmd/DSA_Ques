"""
Q108: Binary Tree Right Side View
===================================
Problem: Imagine standing on the right side of the tree, return
the values of nodes you can see (rightmost node per level).

Example:
    [1,2,3,null,5,null,4] -> [1,3,4]
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def right_side_view(root):
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0: result.append(node.val)  # Rightmost (process right first)
            if node.right: queue.append(node.right)
            if node.left: queue.append(node.left)
    return result

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)),
                       TreeNode(3, None, TreeNode(4)))
    print(right_side_view(root))  # [1,3,4]
