"""
Q341: Find Duplicate Subtrees
================================
Problem: Given root of binary tree, return all duplicate subtrees.
Two subtrees are duplicates if they have the same structure and node values.

Example:
    [1,2,3,4,null,2,4,null,null,4] -> [[2,4],[4]]
"""
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def find_duplicate_subtrees(root):
    count = defaultdict(int)
    result = []
    def serialize(node):
        if not node: return '#'
        s = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        count[s] += 1
        if count[s] == 2: result.append(node)
        return s
    serialize(root)
    return result

def build(vals):
    if not vals: return None
    nodes = [TreeNode(v) if v else None for v in vals]
    for i in range(len(nodes)):
        if nodes[i]:
            if 2*i+1 < len(nodes): nodes[i].left = nodes[2*i+1]
            if 2*i+2 < len(nodes): nodes[i].right = nodes[2*i+2]
    return nodes[0]

if __name__ == "__main__":
    root = build([1,2,3,4,None,2,4,None,None,4])
    dups = find_duplicate_subtrees(root)
    print([node.val for node in dups])  # [4, 2] (duplicated subtrees)
