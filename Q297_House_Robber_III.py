"""
Q297: House Robber III (Tree DP)
==================================
Problem: Houses arranged in a binary tree. Adjacent (parent-child) houses
cannot both be robbed. Find maximum amount you can rob.

Example:
    [3,2,3,null,3,null,1] -> 7  (rob 3,3,1)
    [3,4,5,1,3,null,1]    -> 9  (rob 4,5)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def rob(root):
    def dfs(node):
        # Returns (max without robbing node, max with robbing node)
        if not node: return 0, 0
        l_no, l_yes = dfs(node.left)
        r_no, r_yes = dfs(node.right)
        rob_node = node.val + l_no + r_no
        skip_node = max(l_no, l_yes) + max(r_no, r_yes)
        return skip_node, rob_node

    return max(dfs(root))

if __name__ == "__main__":
    root1 = TreeNode(3,TreeNode(2,None,TreeNode(3)),TreeNode(3,None,TreeNode(1)))
    print(rob(root1))  # 7

    root2 = TreeNode(3,TreeNode(4,TreeNode(1),TreeNode(3)),TreeNode(5,None,TreeNode(1)))
    print(rob(root2))  # 9
