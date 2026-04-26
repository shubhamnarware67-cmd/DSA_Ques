"""
Q106: Construct Binary Tree from Preorder and Inorder Traversal
================================================================
Problem: Given preorder and inorder traversals, construct the binary tree.

Example:
    preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
    Output: Tree rooted at 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder: return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])
    return root

def inorder_traversal(root):
    if not root: return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

if __name__ == "__main__":
    tree = build_tree([3,9,20,15,7], [9,3,15,20,7])
    print(inorder_traversal(tree))  # [9,3,15,20,7]
