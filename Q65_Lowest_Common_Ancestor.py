"""
Q65: Lowest Common Ancestor of BST
=====================================
Problem: Given BST and two nodes p and q, find their LCA.
LCA is the lowest node that has both p and q as descendants.

Example:
    BST root=6, p=2, q=8 -> 6
    BST root=6, p=2, q=4 -> 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

if __name__ == "__main__":
    # Build BST: 6,2,8,0,4,7,9,null,null,3,5
    root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
                       TreeNode(8, TreeNode(7), TreeNode(9)))
    p, q = TreeNode(2), TreeNode(8)
    print(lowest_common_ancestor(root, p, q).val)  # 6
    p2, q2 = TreeNode(2), TreeNode(4)
    print(lowest_common_ancestor(root, p2, q2).val) # 2
