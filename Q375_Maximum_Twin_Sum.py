"""
Q375: Maximum Twin Sum of a Linked List
=========================================
Problem: In linked list of even length, twin of position i is n-1-i.
Find maximum twin sum.

Example:
    [5,4,2,1] -> 6   (5+1=6, 4+2=6 -> max=6)
    [4,2,2,3] -> 7   (4+3=7, 2+2=4 -> max=7)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def pair_sum(head):
    # Collect values
    vals = []
    while head:
        vals.append(head.val); head = head.next
    n = len(vals)
    return max(vals[i] + vals[n-1-i] for i in range(n//2))

def pair_sum_o1_space(head):
    # Reverse second half in-place
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    # Reverse from slow
    prev = None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    max_sum = 0
    left = head
    while prev:
        max_sum = max(max_sum, left.val + prev.val)
        left = left.next; prev = prev.next
    return max_sum

def build(vals):
    h = ListNode(vals[0]); c = h
    for v in vals[1:]: c.next = ListNode(v); c = c.next
    return h

if __name__ == "__main__":
    print(pair_sum(build([5,4,2,1])))           # 6
    print(pair_sum_o1_space(build([4,2,2,3])))  # 7
