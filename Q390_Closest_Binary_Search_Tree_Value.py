"""
Q390: Closest Binary Search Tree Value
=========================================
Problem: Given BST and target (float), find the value in BST closest to target.

Example:
    root=[4,2,5,1,3], target=3.714286 -> 4
    root=[1], target=4.428571         -> 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def closest_value(root, target):
    closest = root.val
    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        root = root.left if target < root.val else root.right
    return closest

def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left = build(vals, 2*i+1); n.right = build(vals, 2*i+2)
    return n

if __name__ == "__main__":
    root = build([4,2,5,1,3])
    print(closest_value(root, 3.714286))  # 4
    print(closest_value(TreeNode(1), 4.428571))  # 1
