"""
Q262: Minimum Cost to Hire K Workers (Greedy + Heap)
=====================================================
Problem: Hire exactly k workers. Pay each worker at least wage[i].
In a group, all workers paid proportional to quality. Min total wages.

Example:
    quality=[10,20,5], wage=[70,50,30], k=2 -> 105.0
    quality=[3,1,10,10,1], wage=[4,8,2,2,7], k=3 -> 30.666...
"""
import heapq

def mincost_to_hire_workers(quality, wage, k):
    workers = sorted((w/q, q) for w, q in zip(wage, quality))
    result = float('inf')
    pool = []  # Max-heap of quality
    total_quality = 0
    for ratio, q in workers:
        heapq.heappush(pool, -q)
        total_quality += q
        if len(pool) > k:
            total_quality += heapq.heappop(pool)  # Remove largest quality
        if len(pool) == k:
            result = min(result, ratio * total_quality)
    return result

if __name__ == "__main__":
    print(mincost_to_hire_workers([10,20,5],[70,50,30],2))        # 105.0
    print(mincost_to_hire_workers([3,1,10,10,1],[4,8,2,2,7],3))  # 30.666...
