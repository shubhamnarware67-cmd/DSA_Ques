"""
Q13: Detect Cycle in Linked List (Floyd's Algorithm)
=====================================================
Problem: Given head of a linked list, determine if the linked list has a cycle.

Example:
    3 -> 2 -> 0 -> -4 (points back to 2)  --> True
    1 -> 2                                  --> False
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == "__main__":
    # Cycle: 3->2->0->-4->2...
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    print(has_cycle(n1))  # True

    # No cycle
    a, b = ListNode(1), ListNode(2)
    a.next = b
    print(has_cycle(a))   # False
