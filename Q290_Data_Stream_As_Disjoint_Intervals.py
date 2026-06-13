"""
Q290: Data Stream as Disjoint Intervals
=========================================
Problem: Add integers from data stream and return sorted disjoint intervals.

Example:
    add(1)   -> [[1,1]]
    add(3)   -> [[1,1],[3,3]]
    add(7)   -> [[1,1],[3,3],[7,7]]
    add(2)   -> [[1,3],[7,7]]
    add(6)   -> [[1,3],[6,7]]
"""
import bisect

class SummaryRanges:
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        new = [val, val]
        merged = []
        inserted = False
        for interval in self.intervals:
            if interval[1] + 1 < new[0]:
                merged.append(interval)
            elif new[1] + 1 < interval[0]:
                if not inserted: merged.append(new); inserted = True
                merged.append(interval)
            else:
                new[0] = min(new[0], interval[0])
                new[1] = max(new[1], interval[1])
        if not inserted: merged.append(new)
        self.intervals = merged

    def getIntervals(self):
        return self.intervals

if __name__ == "__main__":
    sr = SummaryRanges()
    for v in [1,3,7,2,6]:
        sr.addNum(v)
        print(sr.getIntervals())
    # [[1,1]], [[1,1],[3,3]], [[1,1],[3,3],[7,7]], [[1,3],[7,7]], [[1,3],[6,7]]
