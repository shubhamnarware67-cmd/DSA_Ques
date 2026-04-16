"""
Q61: Palindrome Linked List
============================
Problem: Given the head of a linked list, return True if it is a palindrome.
O(n) time, O(1) space using slow/fast pointer + reverse.

Example:
    1->2->2->1 -> True
    1->2       -> False
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse second half
    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    # Compare
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

def build(vals):
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]: cur.next = ListNode(v); cur = cur.next
    return head

if __name__ == "__main__":
    print(is_palindrome(build([1,2,2,1])))  # True
    print(is_palindrome(build([1,2])))      # False
    print(is_palindrome(build([1,2,3,2,1])))# True
