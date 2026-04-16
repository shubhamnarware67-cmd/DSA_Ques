"""
Q63: Validate Binary Search Tree
==================================
Problem: Given root of binary tree, determine if it is a valid BST.
Valid BST: left < node < right (recursively).

Example:
    [2,1,3]   -> True
    [5,1,4,null,null,3,6] -> False
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node: return True
        if not (min_val < node.val < max_val): return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(root1))  # True
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(root2))  # False
