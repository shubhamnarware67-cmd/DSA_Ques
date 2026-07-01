"""
Q367: Reorganize String (Greedy + Heap)
=========================================
Problem: Rearrange string so no two adjacent characters are the same.
Return "" if impossible.

Example:
    "aab"  -> "aba"
    "aaab" -> ""
"""
import heapq
from collections import Counter

def reorganize_string(s):
    freq = Counter(s)
    heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(heap)
    result = []
    while len(heap) >= 2:
        cnt1, ch1 = heapq.heappop(heap)
        cnt2, ch2 = heapq.heappop(heap)
        result.extend([ch1, ch2])
        if cnt1 + 1 < 0: heapq.heappush(heap, (cnt1+1, ch1))
        if cnt2 + 1 < 0: heapq.heappush(heap, (cnt2+1, ch2))
    if heap:
        cnt, ch = heap[0]
        if -cnt > 1: return ""
        result.append(ch)
    return "".join(result)

if __name__ == "__main__":
    print(reorganize_string("aab"))   # "aba"
    print(reorganize_string("aaab"))  # ""
    print(reorganize_string("vvvlo")) # "vlvov" or similar
