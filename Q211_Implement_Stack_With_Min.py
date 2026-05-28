"""
Q211: Implement Stack with O(1) Min (No Extra Stack)
======================================================
Problem: Design a stack supporting push, pop, top, and getMin
in O(1) using only ONE stack (encode min in values).

Example:
    push(5),push(3),push(7),push(2)
    getMin()->2, pop(), getMin()->3
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val):
        if val <= self.min_val:
            self.stack.append(self.min_val)  # Save old min
            self.min_val = val
        self.stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_val:
            self.min_val = self.stack.pop()  # Restore old min

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_val

if __name__ == "__main__":
    ms = MinStack()
    ms.push(5); ms.push(3); ms.push(7); ms.push(2)
    print(ms.getMin())  # 2
    ms.pop()
    print(ms.getMin())  # 3
    ms.pop()
    print(ms.getMin())  # 3
    ms.pop()
    print(ms.getMin())  # 5
