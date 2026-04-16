"""
Q64: Balanced Binary Tree
==========================
Problem: Given binary tree, determine if it is height-balanced
(depth of two subtrees never differs by more than one).

Example:
    [3,9,20,null,null,15,7] -> True
    [1,2,2,3,3,null,null,4,4] -> False
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def is_balanced(root):
    def height(node):
        if not node: return 0
        lh = height(node.left)
        if lh == -1: return -1
        rh = height(node.right)
        if rh == -1: return -1
        if abs(lh - rh) > 1: return -1
        return 1 + max(lh, rh)
    return height(root) != -1

if __name__ == "__main__":
    root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(is_balanced(root1))  # True
    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)))
    print(is_balanced(root2))  # False
