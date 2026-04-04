"""
Q2: Reverse a Linked List
=========================
Problem: Given the head of a singly linked list, reverse the list,
and return the reversed list.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def list_to_arr(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def arr_to_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    head = arr_to_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    print(list_to_arr(reversed_head))  # [5, 4, 3, 2, 1]
