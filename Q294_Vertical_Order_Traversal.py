"""
Q294: Vertical Order Traversal of Binary Tree
===============================================
Problem: Return vertical order traversal column by column.
Within same position, sort by row then value.

Example:
    [3,9,20,null,null,15,7] -> [[9],[3,15],[20],[7]]
    [1,2,3,4,5,6,7]         -> [[4],[2],[1,5,6],[3],[7]]
"""
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def vertical_traversal(root):
    cols = defaultdict(list)
    queue = deque([(root, 0, 0)])
    while queue:
        node, row, col = queue.popleft()
        cols[col].append((row, node.val))
        if node.left:  queue.append((node.left,  row+1, col-1))
        if node.right: queue.append((node.right, row+1, col+1))
    return [[v for _, v in sorted(cols[c])] for c in sorted(cols)]

if __name__ == "__main__":
    root1 = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print(vertical_traversal(root1))  # [[9],[3,15],[20],[7]]
