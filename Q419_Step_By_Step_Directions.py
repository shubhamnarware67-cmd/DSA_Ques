"""
Q419: Step-By-Step Directions From a Binary Tree Node to Another
==================================================================
Problem: Given root and start/dest values, return shortest path string
(U=up, L=left, R=right).

Example:
    root=[5,1,2,3,null,6,4], startValue=3, destValue=6 -> "UURL"
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def get_directions(root, startValue, destValue):
    def find_path(node, target, path):
        if not node: return False
        if node.val == target: return True
        path.append('L')
        if find_path(node.left, target, path): return True
        path.pop()
        path.append('R')
        if find_path(node.right, target, path): return True
        path.pop()
        return False

    path_to_start, path_to_dest = [], []
    find_path(root, startValue, path_to_start)
    find_path(root, destValue, path_to_dest)

    i = 0
    while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
        i += 1

    return 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])

def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left = build(vals, 2*i+1); n.right = build(vals, 2*i+2)
    return n

if __name__ == "__main__":
    root = build([5,1,2,3,None,6,4])
    print(get_directions(root, 3, 6))  # "UURL"
