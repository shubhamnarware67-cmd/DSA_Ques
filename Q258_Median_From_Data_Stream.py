"""
Q258: Find Median from Data Stream (Two Heaps)
================================================
Problem: Design class supporting addNum(num) and findMedian() in O(log n)
and O(1) respectively using two heaps.

Example:
    addNum(1), addNum(2), findMedian() -> 1.5
    addNum(3), findMedian() -> 2.0
"""
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap (negated): lower half
        self.large = []  # Min-heap: upper half

    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1); mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0
    mf.addNum(4)
    print(mf.findMedian())  # 2.5
