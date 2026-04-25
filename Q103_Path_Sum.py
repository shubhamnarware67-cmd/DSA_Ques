"""
Q103: Path Sum
==============
Problem: Given root and targetSum, return True if there is a root-to-leaf
path such that adding up all values along the path equals targetSum.

Example:
    target=22, tree has path 5->4->11->2 = 22 -> True
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def has_path_sum(root, targetSum):
    if not root: return False
    if not root.left and not root.right:
        return root.val == targetSum
    return (has_path_sum(root.left, targetSum - root.val) or
            has_path_sum(root.right, targetSum - root.val))

if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                       TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    print(has_path_sum(root, 22))  # True
    print(has_path_sum(root, 5))   # False
