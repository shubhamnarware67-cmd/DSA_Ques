"""
Q126: Merge K Sorted Linked Lists (Min Heap)
=============================================
Problem: Merge k sorted linked lists into one sorted list.

Example:
    [[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next
    def __lt__(self, other):
        return self.val < other.val

def merge_k_lists(lists):
    heap = []
    for node in lists:
        if node: heapq.heappush(heap, node)
    dummy = curr = ListNode(0)
    while heap:
        node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next: heapq.heappush(heap, node.next)
    return dummy.next

def to_list(node):
    res = []
    while node: res.append(node.val); node = node.next
    return res

def build(vals):
    if not vals: return None
    head = ListNode(vals[0]); curr = head
    for v in vals[1:]: curr.next = ListNode(v); curr = curr.next
    return head

if __name__ == "__main__":
    lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
    print(to_list(merge_k_lists(lists)))  # [1,1,2,3,4,4,5,6]
