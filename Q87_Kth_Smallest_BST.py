"""
Q87: Kth Smallest Element in BST
==================================
Problem: Given root of BST and integer k, return kth smallest value.

Example:
    BST=[3,1,4,null,2], k=1 -> 1
    BST=[5,3,6,2,4,null,null,1], k=3 -> 3
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def kth_smallest(root, k):
    stack = []
    curr = root
    count = 0
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(kth_smallest(root, 1))  # 1
    print(kth_smallest(root, 2))  # 2
    print(kth_smallest(root, 3))  # 3
