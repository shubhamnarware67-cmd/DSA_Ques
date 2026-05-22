"""
Q199: Sliding Window Median (Two Heaps)
=========================================
Problem: Given array and window size k, find median of each window.

Example:
    nums=[1,3,-1,-3,5,3,6,7], k=3 -> [1,-1,-1,3,5,6]
"""
import heapq
from collections import defaultdict

def median_sliding_window(nums, k):
    small = []  # Max-heap (negated)
    large = []  # Min-heap
    result = []
    invalid = defaultdict(int)

    def get_median():
        if k % 2 == 0:
            return (-small[0] + large[0]) / 2
        return float(-small[0])

    def balance():
        while len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        while len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

    for i, num in enumerate(nums):
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(large, num)
        balance()

        if i >= k - 1:
            result.append(get_median())
            out = nums[i - k + 1]
            invalid[out] += 1
            # Lazy removal
            if out <= -small[0]:
                while small and invalid[-small[0]] > 0:
                    invalid[-small[0]] -= 1
                    heapq.heappop(small)
            else:
                while large and invalid[large[0]] > 0:
                    invalid[large[0]] -= 1
                    heapq.heappop(large)
            balance()
    return result

if __name__ == "__main__":
    print(median_sliding_window([1,3,-1,-3,5,3,6,7], 3))  # [1,-1,-1,3,5,6]
    print(median_sliding_window([1,2,3,4,2,3,1,4,2], 3))  # [2,3,3,3,2,3,2]
