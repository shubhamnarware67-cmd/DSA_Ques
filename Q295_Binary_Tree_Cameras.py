"""
Q295: Binary Tree Cameras (Greedy DFS)
========================================
Problem: Place cameras on nodes to monitor all nodes (camera monitors itself,
parent, and children). Find minimum cameras needed.

Example:
    [0,0,null,0,0] -> 1
    [0,0,null,0,null,0,null,null,0] -> 2
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def min_camera_cover(root):
    cameras = [0]
    # Returns: 0=not covered, 1=covered no camera, 2=has camera
    def dfs(node):
        if not node: return 1
        left, right = dfs(node.left), dfs(node.right)
        if left == 0 or right == 0:
            cameras[0] += 1
            return 2
        if left == 2 or right == 2:
            return 1
        return 0

    if dfs(root) == 0:
        cameras[0] += 1
    return cameras[0]

if __name__ == "__main__":
    root1 = TreeNode(0,TreeNode(0,None,TreeNode(0,TreeNode(0))))
    print(min_camera_cover(root1))  # 1

    root2 = TreeNode(0,TreeNode(0,None,TreeNode(0,None,TreeNode(0,None,TreeNode(0)))))
    print(min_camera_cover(root2))  # 2
