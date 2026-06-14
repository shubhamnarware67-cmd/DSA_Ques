"""
Q299: Path Sum III (Prefix Sum + DFS)
=======================================
Problem: Count paths in binary tree that sum to targetSum.
Path doesn't need to start/end at root/leaf.

Example:
    root=[10,5,-3,3,2,null,11,3,-2,null,1], targetSum=8 -> 3
"""
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def path_sum(root, targetSum):
    prefix = defaultdict(int)
    prefix[0] = 1
    result = [0]

    def dfs(node, curr_sum):
        if not node: return
        curr_sum += node.val
        result[0] += prefix[curr_sum - targetSum]
        prefix[curr_sum] += 1
        dfs(node.left, curr_sum)
        dfs(node.right, curr_sum)
        prefix[curr_sum] -= 1

    dfs(root, 0)
    return result[0]

if __name__ == "__main__":
    root = TreeNode(10,
                    TreeNode(5,TreeNode(3,TreeNode(3),TreeNode(-2)),
                               TreeNode(2,None,TreeNode(1))),
                    TreeNode(-3,None,TreeNode(11)))
    print(path_sum(root, 8))  # 3
