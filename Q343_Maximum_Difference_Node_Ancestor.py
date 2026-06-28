"""
Q343: Maximum Difference Between Node and Ancestor
====================================================
Problem: Find maximum abs difference between a node and any ancestor.

Example:
    [8,3,10,1,6,null,14,null,null,4,7,13] -> 7
    [1,null,2,null,0,3] -> 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def max_ancestor_diff(root):
    def dfs(node, lo, hi):
        if not node: return hi - lo
        lo = min(lo, node.val)
        hi = max(hi, node.val)
        return max(dfs(node.left, lo, hi), dfs(node.right, lo, hi))
    return dfs(root, root.val, root.val)

if __name__ == "__main__":
    root = TreeNode(8,
                    TreeNode(3,TreeNode(1),TreeNode(6,TreeNode(4),TreeNode(7))),
                    TreeNode(10,None,TreeNode(14,TreeNode(13))))
    print(max_ancestor_diff(root))  # 7
