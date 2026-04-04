"""
Q8: Invert Binary Tree
=======================
Problem: Given the root of a binary tree, invert the tree,
and return its root.

Example:
         4                 4
       /   \    -->      /   \
      2     7           7     2
     / \   / \         / \   / \
    1   3 6   9       9   6 3   1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                       TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = invert_tree(root)
    print(inorder(inverted))  # [9, 7, 6, 4, 3, 2, 1]
