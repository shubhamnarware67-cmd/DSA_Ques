"""
Q102: Symmetric Tree
=====================
Problem: Given root of binary tree, check if it is a mirror of itself.

Example:
    [1,2,2,3,4,4,3] -> True
    [1,2,2,null,3,null,3] -> False
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def is_symmetric(root):
    def mirror(l, r):
        if not l and not r: return True
        if not l or not r: return False
        return l.val == r.val and mirror(l.left, r.right) and mirror(l.right, r.left)
    return mirror(root.left, root.right)

if __name__ == "__main__":
    r1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                     TreeNode(2, TreeNode(4), TreeNode(3)))
    print(is_symmetric(r1))  # True
    r2 = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                     TreeNode(2, None, TreeNode(3)))
    print(is_symmetric(r2))  # False
