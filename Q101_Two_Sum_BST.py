"""
Q101: Two Sum IV - Input is a BST
===================================
Problem: Given root of BST and integer k, return True if there exist
two elements in the BST such that their sum equals k.

Example:
    BST=[5,3,6,2,4,null,7], k=9  -> True
    BST=[5,3,6,2,4,null,7], k=28 -> False
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def find_target(root, k):
    seen = set()
    def dfs(node):
        if not node: return False
        if k - node.val in seen: return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)

if __name__ == "__main__":
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)),
                       TreeNode(6, None, TreeNode(7)))
    print(find_target(root, 9))   # True  (2+7)
    print(find_target(root, 28))  # False
