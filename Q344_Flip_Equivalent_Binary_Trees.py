"""
Q344: Flip Equivalent Binary Trees
=====================================
Problem: Two binary trees are flip equivalent if we can flip (swap children)
any number of nodes to make them identical. Check if two trees are flip equiv.

Example:
    root1=[1,2,3,4,5,6,null,null,null,7,8], root2=[1,3,2,null,6,4,5,null,null,null,null,8,7] -> True
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def flip_equiv(root1, root2):
    if not root1 and not root2: return True
    if not root1 or not root2: return False
    if root1.val != root2.val: return False

    # No flip
    no_flip = (flip_equiv(root1.left, root2.left) and
               flip_equiv(root1.right, root2.right))
    # Flip
    flip = (flip_equiv(root1.left, root2.right) and
            flip_equiv(root1.right, root2.left))
    return no_flip or flip

if __name__ == "__main__":
    # Build trees and test
    r1 = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(7),TreeNode(8))),
                    TreeNode(3,TreeNode(6)))
    r2 = TreeNode(1,TreeNode(3,None,TreeNode(6)),
                    TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(8),TreeNode(7))))
    print(flip_equiv(r1, r2))  # True
