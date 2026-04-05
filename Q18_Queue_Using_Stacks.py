"""
Q18: Implement Queue Using Stacks
===================================
Problem: Implement a first-in-first-out (FIFO) queue using only two stacks.

Supported: push(x), pop(), peek(), empty()
"""

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

if __name__ == "__main__":
    q = MyQueue()
    q.push(1); q.push(2)
    print(q.peek())   # 1
    print(q.pop())    # 1
    print(q.empty())  # False
