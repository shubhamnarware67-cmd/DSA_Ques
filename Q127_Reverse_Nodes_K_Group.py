"""
Q127: Reverse Nodes in k-Group
================================
Problem: Given linked list, reverse nodes in groups of k.
If remaining nodes < k, leave them as is.

Example:
    [1,2,3,4,5], k=2 -> [2,1,4,3,5]
    [1,2,3,4,5], k=3 -> [3,2,1,4,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = get_kth(group_prev, k)
        if not kth: break
        group_next = kth.next
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            curr.next, prev, curr = prev, curr, curr.next
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
    return dummy.next

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next; k -= 1
    return curr

def to_list(head):
    res = []
    while head: res.append(head.val); head = head.next
    return res

def build(vals):
    head = ListNode(vals[0]); curr = head
    for v in vals[1:]: curr.next = ListNode(v); curr = curr.next
    return head

if __name__ == "__main__":
    print(to_list(reverse_k_group(build([1,2,3,4,5]), 2)))  # [2,1,4,3,5]
    print(to_list(reverse_k_group(build([1,2,3,4,5]), 3)))  # [3,2,1,4,5]
