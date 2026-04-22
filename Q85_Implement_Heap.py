"""
Q85: Implement Min-Heap from Scratch
======================================
Problem: Build a min-heap with insert, extract_min, and heapify operations.

A min-heap is a complete binary tree where parent <= children.
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap: return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = 2*i+1, 2*i+2
            if left < n and self.heap[left] < self.heap[smallest]: smallest = left
            if right < n and self.heap[right] < self.heap[smallest]: smallest = right
            if smallest == i: break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

if __name__ == "__main__":
    h = MinHeap()
    for v in [5, 3, 8, 1, 4]:
        h.insert(v)
    print([h.extract_min() for _ in range(5)])  # [1,3,4,5,8]
