"""
Q292: Maximum Sum BST in Binary Tree
=======================================
Problem: Given binary tree, find maximum sum of all keys of any subtree
which is also a BST.

Example:
    [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6] -> 20
    [4,3,null,1,2] -> 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def max_sum_bst(root):
    result = [0]
    def dfs(node):
        # Returns (is_bst, min_val, max_val, sum)
        if not node: return True, float('inf'), float('-inf'), 0
        lbst, lmin, lmax, lsum = dfs(node.left)
        rbst, rmin, rmax, rsum = dfs(node.right)
        if lbst and rbst and lmax < node.val < rmin:
            total = lsum + rsum + node.val
            result[0] = max(result[0], total)
            return True, min(lmin, node.val), max(rmax, node.val), total
        return False, 0, 0, 0
    dfs(root)
    return result[0]

if __name__ == "__main__":
    root = TreeNode(1,TreeNode(4,TreeNode(2),TreeNode(4)),
                      TreeNode(3,TreeNode(2),TreeNode(5,TreeNode(4),TreeNode(6))))
    print(max_sum_bst(root))  # 20
