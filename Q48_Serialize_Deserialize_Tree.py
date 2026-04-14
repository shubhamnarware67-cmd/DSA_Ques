"""
Q48: Serialize and Deserialize Binary Tree
==========================================
Problem: Design an algorithm to serialize and deserialize a binary tree.

Example:
    Tree: 1 -> [2, 3] -> [null, null, 4, 5]
    Serialized: "1,2,N,N,3,4,N,N,5,N,N"
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append('N')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)

    def deserialize(self, data):
        vals = iter(data.split(','))
        def dfs():
            val = next(vals)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    s = codec.serialize(root)
    print("Serialized:", s)
    restored = codec.deserialize(s)
    print("Reserialized:", codec.serialize(restored))
