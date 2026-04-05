"""
Q21: Binary Search Tree - Insert & Search
==========================================
Problem: Implement insert and search operations in a BST.

BST Property: left child < parent < right child

Example:
    Insert: 5, 3, 7, 1, 4
    Search: 4 -> True, 6 -> False
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

if __name__ == "__main__":
    bst = BST()
    for v in [5, 3, 7, 1, 4]:
        bst.insert(v)
    print(bst.search(4))  # True
    print(bst.search(6))  # False
