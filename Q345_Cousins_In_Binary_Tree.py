"""
Q345: Cousins in Binary Tree
==============================
Problem: Two nodes are cousins if they are at the same depth but have
different parents. Return True if x and y are cousins.

Example:
    root=[1,2,3,4], x=4, y=3 -> False  (different depths)
    root=[1,2,3,null,4,null,5], x=5, y=4 -> True
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def is_cousins(root, x, y):
    queue = deque([(root, None, 0)])
    x_info = y_info = None
    while queue:
        node, parent, depth = queue.popleft()
        if node.val == x: x_info = (parent, depth)
        if node.val == y: y_info = (parent, depth)
        if x_info and y_info:
            return x_info[1] == y_info[1] and x_info[0] != y_info[0]
        if node.left:  queue.append((node.left,  node, depth+1))
        if node.right: queue.append((node.right, node, depth+1))
    return False

if __name__ == "__main__":
    r1 = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3))
    print(is_cousins(r1, 4, 3))  # False

    r2 = TreeNode(1,TreeNode(2,None,TreeNode(4)),TreeNode(3,None,TreeNode(5)))
    print(is_cousins(r2, 5, 4))  # True
