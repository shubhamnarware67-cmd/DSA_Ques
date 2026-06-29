"""
Q347: Convert Sorted List to BST (Height-Balanced)
====================================================
Problem: Convert sorted linked list to height-balanced BST.

Example:
    [-10,-3,0,5,9] -> [0,-3,9,-10,null,5] (one valid answer)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

def sorted_list_to_bst(head):
    def find_mid(head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow; slow = slow.next; fast = fast.next.next
        if prev: prev.next = None
        return slow

    if not head: return None
    mid = find_mid(head)
    node = TreeNode(mid.val)
    if head == mid: return node
    node.left  = sorted_list_to_bst(head)
    node.right = sorted_list_to_bst(mid.next)
    return node

def inorder(root):
    if not root: return []
    return inorder(root.left)+[root.val]+inorder(root.right)

if __name__ == "__main__":
    vals = [-10,-3,0,5,9]
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]: cur.next = ListNode(v); cur = cur.next
    root = sorted_list_to_bst(head)
    print(inorder(root))  # [-10,-3,0,5,9]
