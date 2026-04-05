"""
Q17: Implement Stack Using Queues
==================================
Problem: Implement a last-in-first-out (LIFO) stack using only two queues.

Supported operations: push(x), pop(), top(), empty()
"""
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())   # 2
    print(stack.pop())   # 2
    print(stack.empty()) # False
