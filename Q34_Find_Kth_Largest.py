"""
Q34: Kth Largest Element in an Array
======================================
Problem: Given an integer array and an integer k,
return the kth largest element in the array.

Example:
    nums = [3,2,1,5,6,4], k = 2
    Output: 5
"""
import heapq

def find_kth_largest(nums, k):
    # Min-heap of size k
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

# QuickSelect O(n) average
def find_kth_largest_qs(nums, k):
    def quickselect(l, r, k):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p == k: return nums[p]
        elif p < k: return quickselect(p+1, r, k)
        else: return quickselect(l, p-1, k)
    return quickselect(0, len(nums)-1, len(nums)-k)

if __name__ == "__main__":
    print(find_kth_largest([3,2,1,5,6,4], 2))     # 5
    print(find_kth_largest_qs([3,2,3,1,2,4,5,5,6], 4))  # 4
