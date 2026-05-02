"""
Q130: Remove Nth Node From End of List
========================================
Problem: Given linked list and n, remove the nth node from the end
in one pass using two pointers.

Example:
    [1,2,3,4,5], n=2 -> [1,2,3,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

def build(vals):
    h = ListNode(vals[0]); c = h
    for v in vals[1:]: c.next = ListNode(v); c = c.next
    return h

def to_list(node):
    res = []
    while node: res.append(node.val); node = node.next
    return res

if __name__ == "__main__":
    print(to_list(remove_nth_from_end(build([1,2,3,4,5]), 2)))  # [1,2,3,5]
    print(to_list(remove_nth_from_end(build([1]), 1)))           # []
