"""
Q233: Implement Deque (Double Ended Queue) from Scratch
========================================================
Problem: Build a deque using a doubly linked list supporting:
addFront, addRear, removeFront, removeRear, peekFront, peekRear — all O(1).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

class MyDeque:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def addFront(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def addRear(self, val):
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def removeFront(self):
        if not self.head: return None
        val = self.head.val
        self.head = self.head.next
        if self.head: self.head.prev = None
        else: self.tail = None
        self.size -= 1
        return val

    def removeRear(self):
        if not self.tail: return None
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail: self.tail.next = None
        else: self.head = None
        self.size -= 1
        return val

    def peekFront(self): return self.head.val if self.head else None
    def peekRear(self):  return self.tail.val if self.tail else None
    def isEmpty(self):   return self.size == 0

if __name__ == "__main__":
    dq = MyDeque()
    dq.addRear(1); dq.addRear(2); dq.addFront(0)
    print(dq.peekFront(), dq.peekRear())  # 0 2
    print(dq.removeFront())               # 0
    print(dq.removeRear())                # 2
    print(dq.peekFront())                 # 1
