"""
Q351: K-th Largest Sum Subarray (Min Heap + Prefix Sums)
=========================================================
Problem: Given array, find the kth largest subarray sum.

Example:
    nums=[2,-1,3], k=2 -> 4  (subarrays: [2]=2,[-1]=-1,[3]=3,[2,-1]=1,[2,-1,3]=4,[-1,3]=2)
    sorted desc: [4,3,2,2,1,-1] -> kth=2 -> 3
"""
import heapq

def kth_largest_sum(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]

    # All subarray sums
    heap = []
    for i in range(1, n+1):
        for j in range(i, n+1):
            s = prefix[j] - prefix[i-1]
            if len(heap) < k:
                heapq.heappush(heap, s)
            elif s > heap[0]:
                heapq.heapreplace(heap, s)
    return heap[0]

if __name__ == "__main__":
    print(kth_largest_sum([2,-1,3], 2))   # 3
    print(kth_largest_sum([1,2,3,4], 3))  # 6
