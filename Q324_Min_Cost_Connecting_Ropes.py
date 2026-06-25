"""
Q324: Minimum Cost to Connect Ropes (Greedy + Min Heap)
=========================================================
Problem: Connect ropes with cost = sum of two lengths. Minimize total cost.
(Huffman coding variant)

Example:
    [4,3,2,6] -> 29
    [1,2,3,4,5] -> 33
"""
import heapq

def connect_ropes(ropes):
    heapq.heapify(ropes)
    total = 0
    while len(ropes) > 1:
        a = heapq.heappop(ropes)
        b = heapq.heappop(ropes)
        cost = a + b
        total += cost
        heapq.heappush(ropes, cost)
    return total

if __name__ == "__main__":
    print(connect_ropes([4,3,2,6]))    # 29
    print(connect_ropes([1,2,3,4,5])) # 33
    print(connect_ropes([5]))          # 0
