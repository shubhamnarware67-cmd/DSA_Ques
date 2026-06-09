"""
Q269: Find Right Interval (Binary Search)
==========================================
Problem: For each interval, find index of the interval with minimum start
that is >= current interval's end. Return -1 if none.

Example:
    [[1,2]]          -> [-1]
    [[3,4],[2,3],[1,2]] -> [-1,0,1]
    [[1,4],[2,3],[3,4]] -> [-1,2,-1]
"""
import bisect

def find_right_interval(intervals):
    starts = sorted((s, i) for i, (s, e) in enumerate(intervals))
    start_vals = [s for s, _ in starts]
    result = []
    for s, e in intervals:
        pos = bisect.bisect_left(start_vals, e)
        if pos < len(starts):
            result.append(starts[pos][1])
        else:
            result.append(-1)
    return result

if __name__ == "__main__":
    print(find_right_interval([[1,2]]))               # [-1]
    print(find_right_interval([[3,4],[2,3],[1,2]]))   # [-1,0,1]
    print(find_right_interval([[1,4],[2,3],[3,4]]))   # [-1,2,-1]
