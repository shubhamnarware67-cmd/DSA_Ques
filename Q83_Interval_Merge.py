"""
Q83: Merge Intervals
=====================
Problem: Given array of intervals, merge all overlapping intervals.

Example:
    [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
    [[1,4],[4,5]]               -> [[1,5]]
"""

def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1,4],[4,5]]))                  # [[1,5]]
