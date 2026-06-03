"""
Q239: AVL Tree (Self-Balancing BST)
=====================================
Problem: Implement AVL Tree with insert and rotation operations.
AVL trees maintain height balance factor in {-1, 0, 1} at every node.

Example:
    Insert: 10, 20, 30  (triggers left rotation)
    Inorder: [10, 20, 30]  Tree balanced at 20
"""

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_right(self, z):
        y = z.left; T3 = y.right
        y.right = z; z.left = T3
        self.update_height(z); self.update_height(y)
        return y

    def rotate_left(self, z):
        y = z.right; T2 = y.left
        y.left = z; z.right = T2
        self.update_height(z); self.update_height(y)
        return y

    def insert(self, root, key):
        if not root: return AVLNode(key)
        if key < root.val: root.left = self.insert(root.left, key)
        elif key > root.val: root.right = self.insert(root.right, key)
        else: return root
        self.update_height(root)
        balance = self.get_balance(root)
        if balance > 1 and key < root.left.val:   return self.rotate_right(root)
        if balance < -1 and key > root.right.val: return self.rotate_left(root)
        if balance > 1 and key > root.left.val:
            root.left = self.rotate_left(root.left); return self.rotate_right(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rotate_right(root.right); return self.rotate_left(root)
        return root

    def inorder(self, root):
        return self.inorder(root.left)+[root.val]+self.inorder(root.right) if root else []

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    for v in [10,20,30,40,50,25]:
        root = avl.insert(root, v)
    print("Inorder:", avl.inorder(root))  # [10,20,25,30,40,50]
    print("Root:", root.val)              # 30 (balanced)
