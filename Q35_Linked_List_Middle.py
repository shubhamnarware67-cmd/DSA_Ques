"""
Q35: Middle of the Linked List
================================
Problem: Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example:
    1->2->3->4->5  -> Node 3
    1->2->3->4     -> Node 3
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    def build(vals):
        head = ListNode(vals[0])
        cur = head
        for v in vals[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head

    print(to_list(middle_node(build([1,2,3,4,5]))))  # [3,4,5]
    print(to_list(middle_node(build([1,2,3,4]))))    # [3,4]
