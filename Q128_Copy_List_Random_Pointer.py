"""
Q128: Copy List with Random Pointer
=====================================
Problem: Linked list where each node has next and random pointer.
Deep copy the list.

Example:
    [[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x; self.next = next; self.random = random

def copy_random_list(head):
    if not head: return None
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        if curr.next: old_to_new[curr].next = old_to_new[curr.next]
        if curr.random: old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next
    return old_to_new[head]

if __name__ == "__main__":
    n1, n2, n3 = Node(7), Node(13), Node(1)
    n1.next = n2; n2.next = n3
    n2.random = n1; n3.random = n1
    cloned = copy_random_list(n1)
    print(cloned.val, cloned is not n1)        # 7 True
    print(cloned.next.random.val)              # 7
