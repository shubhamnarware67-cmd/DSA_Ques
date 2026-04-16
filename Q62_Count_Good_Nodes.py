"""
Q62: Count Good Nodes in Binary Tree
=====================================
Problem: A node X is good if in the path from root to X, there are
no nodes with a value greater than X. Count all good nodes.

Example:
    Tree: 3->[1,4->[1,5]]
    Good nodes: 3, 4, 5 -> Output: 4
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def good_nodes(root):
    def dfs(node, max_so_far):
        if not node: return 0
        count = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return count + dfs(node.left, new_max) + dfs(node.right, new_max)
    return dfs(root, float('-inf'))

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, TreeNode(3)),
                       TreeNode(4, TreeNode(1), TreeNode(5)))
    print(good_nodes(root))  # 4
