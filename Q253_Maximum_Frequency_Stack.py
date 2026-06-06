"""
Q253: Maximum Frequency Stack (FreqStack)
==========================================
Problem: Design a stack that returns the most frequently occurring element
on pop(). Ties broken by most recently pushed.

Example:
    push: 5,7,5,7,4,5
    pop() -> 5 (freq 3), pop() -> 7 (freq 2), pop() -> 5 (freq 2)
"""
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)  # freq -> [elements]
        self.max_freq = 0

    def push(self, val):
        self.freq[val] += 1
        f = self.freq[val]
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(val)

    def pop(self):
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val

if __name__ == "__main__":
    fs = FreqStack()
    for v in [5,7,5,7,4,5]: fs.push(v)
    print(fs.pop())  # 5
    print(fs.pop())  # 7
    print(fs.pop())  # 5
    print(fs.pop())  # 4
