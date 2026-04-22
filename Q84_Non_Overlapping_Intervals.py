"""
Q84: Non-overlapping Intervals (Greedy)
=========================================
Problem: Given array of intervals, find minimum number to remove to
make the rest non-overlapping.

Example:
    [[1,2],[2,3],[3,4],[1,3]] -> 1  (remove [1,3])
    [[1,2],[1,2],[1,2]]       -> 2
"""

def erase_overlap_intervals(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start < prev_end:
            count += 1
        else:
            prev_end = end
    return count

if __name__ == "__main__":
    print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
    print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))        # 2
