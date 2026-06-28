"""
Q342: Construct BST from Preorder Traversal
=============================================
Problem: Given preorder traversal of BST, reconstruct the BST.

Example:
    [8,5,1,7,10,12] -> BST rooted at 8
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def bst_from_preorder(preorder):
    idx = [0]
    def build(min_val, max_val):
        if idx[0] == len(preorder): return None
        val = preorder[idx[0]]
        if val < min_val or val > max_val: return None
        node = TreeNode(val)
        idx[0] += 1
        node.left = build(min_val, val)
        node.right = build(val, max_val)
        return node
    return build(float('-inf'), float('inf'))

def inorder(root):
    if not root: return []
    return inorder(root.left) + [root.val] + inorder(root.right)

if __name__ == "__main__":
    root = bst_from_preorder([8,5,1,7,10,12])
    print(inorder(root))  # [1,5,7,8,10,12] — sorted = valid BST
