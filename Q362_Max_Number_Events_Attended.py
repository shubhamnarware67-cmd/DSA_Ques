"""
Q362: Maximum Number of Events That Can Be Attended (Greedy + Heap)
====================================================================
Problem: Events[i]=[start,end]. Each day attend at most 1 event.
Maximize number of events attended.

Example:
    [[1,2],[2,3],[3,4]] -> 3
    [[1,2],[2,3],[3,4],[1,2]] -> 4
"""
import heapq

def max_events(events):
    events.sort()
    heap = []
    count = 0
    day = 1
    i = 0
    n = len(events)
    while i < n or heap:
        if not heap:
            day = events[i][0]
        while i < n and events[i][0] == day:
            heapq.heappush(heap, events[i][1])
            i += 1
        # Attend event ending soonest
        while heap and heap[0] < day:
            heapq.heappop(heap)
        if heap:
            heapq.heappop(heap)
            count += 1
        day += 1
    return count

if __name__ == "__main__":
    print(max_events([[1,2],[2,3],[3,4]]))         # 3
    print(max_events([[1,2],[2,3],[3,4],[1,2]]))   # 4
    print(max_events([[1,4],[4,4],[2,2],[3,4],[1,1]])) # 4
