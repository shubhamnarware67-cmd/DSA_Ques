"""
Q110: Flatten Binary Tree to Linked List
==========================================
Problem: Flatten binary tree to a linked list in-place
(right pointers, left = None, preorder).

Example:
    [1,2,5,3,4,null,6] -> 1->2->3->4->5->6
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def flatten(root):
    curr = root
    while curr:
        if curr.left:
            rightmost = curr.left
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = curr.right
            curr.right = curr.left
            curr.left = None
        curr = curr.right

def to_list(root):
    res = []
    while root: res.append(root.val); root = root.right
    return res

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                       TreeNode(5, None, TreeNode(6)))
    flatten(root)
    print(to_list(root))  # [1,2,3,4,5,6]
