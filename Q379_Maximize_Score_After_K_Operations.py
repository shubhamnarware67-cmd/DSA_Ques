"""
Q379: Maximize Score After K Operations (Greedy + Max Heap)
============================================================
Problem: Choose element, add to score, replace with ceil(v/3).
Maximize score after k operations.

Example:
    nums=[10,10,10,10,10], k=5 -> 50
    nums=[1,10,3,3,3], k=3     -> 17
"""
import heapq, math

def max_kelements(nums, k):
    heap = [-n for n in nums]
    heapq.heapify(heap)
    score = 0
    for _ in range(k):
        v = -heapq.heappop(heap)
        score += v
        heapq.heappush(heap, -math.ceil(v / 3))
    return score

if __name__ == "__main__":
    print(max_kelements([10,10,10,10,10], 5))  # 50
    print(max_kelements([1,10,3,3,3], 3))       # 17
