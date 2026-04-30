"""
Q129: Add Two Numbers (Linked List)
=====================================
Problem: Two non-empty linked lists represent two non-negative integers
(digits stored in reverse). Add and return the sum as a linked list.

Example:
    [2,4,3] + [5,6,4] = [7,0,8]  (342 + 465 = 807)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def add_two_numbers(l1, l2):
    dummy = curr = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry, digit = divmod(total, 10)
        curr.next = ListNode(digit)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
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
    l1, l2 = build([2,4,3]), build([5,6,4])
    print(to_list(add_two_numbers(l1, l2)))  # [7,0,8]
