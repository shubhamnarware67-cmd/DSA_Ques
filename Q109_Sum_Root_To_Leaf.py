"""
Q109: Sum Root to Leaf Numbers
================================
Problem: Each root-to-leaf path represents a number (digits).
Return the total sum of all root-to-leaf numbers.

Example:
    Tree: 1 -> [2, 3]
    Paths: 12 + 13 = 25
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def sum_numbers(root):
    def dfs(node, current):
        if not node: return 0
        current = current * 10 + node.val
        if not node.left and not node.right:
            return current
        return dfs(node.left, current) + dfs(node.right, current)
    return dfs(root, 0)

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sum_numbers(root))  # 25

    root2 = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    print(sum_numbers(root2))  # 1026
