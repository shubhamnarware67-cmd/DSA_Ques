"""
Q406: Count Nodes Equal to Average of Subtree (DFS)
====================================================
Problem: Count nodes where node.val == average (integer division)
of all values in its subtree (including itself).

Example:
    [4,8,5,0,1,null,6] -> 5
    [1] -> 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def average_of_subtree(root):
    result = [0]
    def dfs(node):
        if not node: return 0, 0
        ls, lc = dfs(node.left)
        rs, rc = dfs(node.right)
        total = ls + rs + node.val
        count = lc + rc + 1
        if total // count == node.val:
            result[0] += 1
        return total, count
    dfs(root)
    return result[0]

def build(vals, i=0):
    if i >= len(vals) or vals[i] is None: return None
    n = TreeNode(vals[i])
    n.left = build(vals, 2*i+1); n.right = build(vals, 2*i+2)
    return n

if __name__ == "__main__":
    print(average_of_subtree(build([4,8,5,0,1,None,6])))  # 5
    print(average_of_subtree(TreeNode(1)))                  # 1
