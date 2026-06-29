"""
Q346: Delete Node in a BST
============================
Problem: Given root of BST and key, delete the node and return root.

Example:
    root=[5,3,6,2,4,null,7], key=3 -> [5,4,6,2,null,null,7]
    root=[5,3,6,2,4,null,7], key=0 -> [5,3,6,2,4,null,7]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def delete_node(root, key):
    if not root: return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left: return root.right
        if not root.right: return root.left
        # Find inorder successor (min of right subtree)
        successor = root.right
        while successor.left: successor = successor.left
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)
    return root

def inorder(root):
    if not root: return []
    return inorder(root.left)+[root.val]+inorder(root.right)

if __name__ == "__main__":
    def build(vals, i=0):
        if i>=len(vals) or vals[i] is None: return None
        n=TreeNode(vals[i]); n.left=build(vals,2*i+1); n.right=build(vals,2*i+2)
        return n
    root = build([5,3,6,2,4,None,7])
    root = delete_node(root, 3)
    print(inorder(root))  # [2,4,5,6,7]
