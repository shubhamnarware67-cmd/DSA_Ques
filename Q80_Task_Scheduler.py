"""
Q80: Task Scheduler (Greedy + Heap)
=====================================
Problem: Given tasks and a cooldown n, find minimum intervals needed
to finish all tasks. Identical tasks must be at least n apart.

Example:
    tasks=["A","A","A","B","B","B"], n=2 -> 8
    (A->B->idle->A->B->idle->A->B)
"""
import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    time = 0
    queue = deque()  # (count, available_time)
    while max_heap or queue:
        time += 1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                queue.append((cnt, time + n))
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])
    return time

if __name__ == "__main__":
    print(least_interval(["A","A","A","B","B","B"], 2))  # 8
    print(least_interval(["A","A","A","B","B","B"], 0))  # 6
