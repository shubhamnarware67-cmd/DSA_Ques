"""
Q413: Maximum Subsequence Score (Greedy + Heap)
=================================================
Problem: Pick k indices. Score = sum(nums1[chosen]) * min(nums2[chosen]).
Maximize score.

Example:
    nums1=[1,3,3,2], nums2=[2,1,3,4], k=3 -> 12
    nums1=[4,2,3,1,1], nums2=[7,5,10,9,6], k=1 -> 30
"""
import heapq

def max_score(nums1, nums2, k):
    pairs = sorted(zip(nums2, nums1), reverse=True)
    heap = []
    total = 0
    result = 0
    for n2, n1 in pairs:
        heapq.heappush(heap, n1)
        total += n1
        if len(heap) > k:
            total -= heapq.heappop(heap)
        if len(heap) == k:
            result = max(result, total * n2)
    return result

if __name__ == "__main__":
    print(max_score([1,3,3,2], [2,1,3,4], 3))         # 12
    print(max_score([4,2,3,1,1], [7,5,10,9,6], 1))    # 30
