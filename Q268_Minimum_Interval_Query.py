"""
Q268: Minimum Interval to Include Each Query (Heap + Offline)
==============================================================
Problem: For each query q, find smallest interval [l,r] with l<=q<=r.
Answer is (r-l+1). Return -1 if no such interval.

Example:
    intervals=[[1,4],[2,4],[3,6],[4,4]], queries=[2,3,4,5] -> [3,3,1,4]
"""
import heapq

def min_interval(intervals, queries):
    intervals.sort()
    queries_with_idx = sorted(enumerate(queries), key=lambda x: x[1])
    result = [-1] * len(queries)
    heap = []  # (size, end)
    i = 0
    for idx, q in queries_with_idx:
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(heap, (r-l+1, r))
            i += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            result[idx] = heap[0][0]
    return result

if __name__ == "__main__":
    print(min_interval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))  # [3,3,1,4]
    print(min_interval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))  # [2,-1,4,6]
