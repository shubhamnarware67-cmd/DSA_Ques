"""
Q107: Binary Tree Zigzag Level Order Traversal
================================================
Problem: Return the zigzag level order traversal (left-to-right,
then right-to-left alternately).

Example:
    [3,9,20,null,null,15,7] -> [[3],[20,9],[15,7]]
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def zigzag_level_order(root):
    if not root: return []
    result, queue, left_to_right = [], deque([root]), True
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right: level.append(node.val)
            else: level.appendleft(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right
    return result

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(zigzag_level_order(root))  # [[3],[20,9],[15,7]]
+