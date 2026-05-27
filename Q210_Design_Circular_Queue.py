"""
Q210: Design Circular Queue
============================
Problem: Implement MyCircularQueue with fixed size using array.
Operations: enQueue, deQueue, Front, Rear, isEmpty, isFull.

Example:
    MyCircularQueue(3)
    enQueue(1)->True, enQueue(2)->True, enQueue(3)->True
    enQueue(4)->False, Rear()->3, isFull()->True
    deQueue()->True, enQueue(4)->True, Rear()->4
"""

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.head = self.tail = -1
        self.size = 0
        self.capacity = k

    def enQueue(self, value):
        if self.isFull(): return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return True

    def Front(self): return -1 if self.isEmpty() else self.queue[self.head]
    def Rear(self):  return -1 if self.isEmpty() else self.queue[self.tail]
    def isEmpty(self): return self.size == 0
    def isFull(self):  return self.size == self.capacity

if __name__ == "__main__":
    cq = MyCircularQueue(3)
    print(cq.enQueue(1), cq.enQueue(2), cq.enQueue(3))  # True True True
    print(cq.enQueue(4))   # False
    print(cq.Rear())       # 3
    print(cq.isFull())     # True
    print(cq.deQueue())    # True
    print(cq.enQueue(4))   # True
    print(cq.Rear())       # 4
