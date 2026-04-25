"""
Q104: Diameter of Binary Tree
===============================
Problem: Return the length of the diameter of the tree (longest path
between any two nodes — may not pass through root).

Example:
    [1,2,3,4,5] -> 3  (path: 4->2->1->3 or 5->2->1->3)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def diameter_of_binary_tree(root):
    max_diameter = [0]
    def depth(node):
        if not node: return 0
        left = depth(node.left)
        right = depth(node.right)
        max_diameter[0] = max(max_diameter[0], left + right)
        return 1 + max(left, right)
    depth(root)
    return max_diameter[0]

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(diameter_of_binary_tree(root))  # 3
