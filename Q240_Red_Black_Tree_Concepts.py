"""
Q240: Red-Black Tree (Concepts + Simplified Insert)
======================================================
Problem: Implement simplified Red-Black Tree insertion with recoloring
and rotation rules. RB trees guarantee O(log n) operations.

RB Properties:
1. Every node is Red or Black
2. Root is Black
3. Red nodes have Black children
4. All paths from node to leaves have same Black-height
"""

class RBNode:
    def __init__(self, val, color='R'):
        self.val = val
        self.color = color  # 'R' or 'B'
        self.left = self.right = self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(0, 'B')
        self.root = self.NIL

    def insert(self, val):
        node = RBNode(val)
        node.left = node.right = self.NIL
        parent = None
        curr = self.root
        while curr != self.NIL:
            parent = curr
            if val < curr.val: curr = curr.left
            else: curr = curr.right
        node.parent = parent
        if not parent: self.root = node
        elif val < parent.val: parent.left = node
        else: parent.right = node
        node.color = 'R'
        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'R':
                    node.parent.color = uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent; self._rotate_left(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'R':
                    node.parent.color = uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent; self._rotate_right(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'B'

    def _rotate_left(self, x):
        y = x.right; x.right = y.left
        if y.left != self.NIL: y.left.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def _rotate_right(self, x):
        y = x.left; x.left = y.right
        if y.right != self.NIL: y.right.parent = x
        y.parent = x.parent
        if not x.parent: self.root = y
        elif x == x.parent.right: x.parent.right = y
        else: x.parent.left = y
        y.right = x; x.parent = y

    def inorder(self, node=None, result=None):
        if result is None: result = []; node = self.root
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append((node.val, node.color))
            self.inorder(node.right, result)
        return result

if __name__ == "__main__":
    rbt = RedBlackTree()
    for v in [7,3,18,10,22,8,11,26]:
        rbt.insert(v)
    print("Inorder (val, color):", rbt.inorder())
