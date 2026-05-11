"""
Q165: Kth Largest Element in a Stream
=======================================
Problem: Design class that finds the kth largest element in a stream.
init(k, nums), add(val) -> current kth largest.

Example:
    k=3, nums=[4,5,8,2]
    add(3) -> 4, add(5) -> 5, add(10) -> 8, add(9) -> 8, add(4) -> 8
"""
import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    kl = KthLargest(3, [4,5,8,2])
    print(kl.add(3))   # 4
    print(kl.add(5))   # 5
    print(kl.add(10))  # 8
    print(kl.add(9))   # 8
    print(kl.add(4))   # 8
