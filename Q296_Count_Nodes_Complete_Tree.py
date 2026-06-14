"""
Q296: Count Complete Tree Nodes (O(log^2 n))
=============================================
Problem: Count nodes in a complete binary tree faster than O(n).
Use the property that a complete tree has 2^h nodes in last level (or full subtree).

Example:
    [1,2,3,4,5,6] -> 6
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def count_nodes(root):
    if not root: return 0

    def get_height(node, go_left):
        h = 0
        while node:
            h += 1
            node = node.left if go_left else node.right
        return h

    left_h = get_height(root, True)
    right_h = get_height(root, False)

    if left_h == right_h:
        return (1 << left_h) - 1  # Perfect tree: 2^h - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def build_complete(vals, i=0):
    if i >= len(vals): return None
    node = TreeNode(vals[i])
    node.left  = build_complete(vals, 2*i+1)
    node.right = build_complete(vals, 2*i+2)
    return node

if __name__ == "__main__":
    root = build_complete([1,2,3,4,5,6])
    print(count_nodes(root))  # 6
    print(count_nodes(build_complete([1,2,3,4,5,6,7])))  # 7
