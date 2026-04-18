"""
Q82: Meeting Rooms II (Min Heap)
==================================
Problem: Given array of meeting intervals, find minimum number of
conference rooms required.

Example:
    [[0,30],[5,10],[15,20]] -> 2
    [[7,10],[2,4]]          -> 1
"""
import heapq

def min_meeting_rooms(intervals):
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    heap = []  # End times
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)

if __name__ == "__main__":
    print(min_meeting_rooms([[0,30],[5,10],[15,20]]))  # 2
    print(min_meeting_rooms([[7,10],[2,4]]))            # 1
