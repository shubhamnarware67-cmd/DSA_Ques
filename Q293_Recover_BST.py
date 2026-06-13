"""
Q293: Recover Binary Search Tree
===================================
Problem: Two nodes of BST are swapped. Recover without changing structure.

Example:
    [1,3,null,null,2] -> [3,1,null,null,2]
    [3,1,4,null,null,2] -> [2,1,4,null,null,3]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def recover_tree(root):
    first = second = prev = None

    def inorder(node):
        nonlocal first, second, prev
        if not node: return
        inorder(node.left)
        if prev and prev.val > node.val:
            if not first: first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    first.val, second.val = second.val, first.val

def inorder_vals(root):
    if not root: return []
    return inorder_vals(root.left) + [root.val] + inorder_vals(root.right)

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    print("Before:", inorder_vals(root))  # [1,3,2,4] — 3 and 2 swapped
    recover_tree(root)
    print("After:", inorder_vals(root))   # [1,2,3,4]
