"""
Q449: Range Module (Interval Management)
==========================================
Problem: Track ranges of numbers. addRange, queryRange, removeRange.

Example:
    addRange(10,20), removeRange(14,16), queryRange(10,14) -> True
    queryRange(13,15) -> False
    queryRange(16,17) -> True
"""
import bisect

class RangeModule:
    def __init__(self):
        self.ranges = []  # Sorted list of [start, end) non-overlapping

    def addRange(self, left, right):
        new_ranges = []
        i = 0
        n = len(self.ranges)
        while i < n and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i]); i += 1
        while i < n and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1
        new_ranges.append([left, right])
        new_ranges.extend(self.ranges[i:])
        self.ranges = new_ranges

    def queryRange(self, left, right):
        for s, e in self.ranges:
            if s <= left and right <= e:
                return True
        return False

    def removeRange(self, left, right):
        new_ranges = []
        for s, e in self.ranges:
            if e <= left or s >= right:
                new_ranges.append([s, e])
            else:
                if s < left: new_ranges.append([s, left])
                if e > right: new_ranges.append([right, e])
        self.ranges = new_ranges

if __name__ == "__main__":
    rm = RangeModule()
    rm.addRange(10, 20)
    rm.removeRange(14, 16)
    print(rm.queryRange(10, 14))  # True
    print(rm.queryRange(13, 15)) # False
    print(rm.queryRange(16, 17)) # True
