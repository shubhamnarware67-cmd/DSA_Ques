"""
Q121: Top K Frequent Elements (Bucket Sort)
=============================================
Problem: Given array and k, return the k most frequent elements.
Must be better than O(n log n).

Example:
    [1,1,1,2,2,3], k=2 -> [1,2]
"""
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in range(len(buckets)-1, 0, -1):
        result.extend(buckets[i])
        if len(result) >= k:
            return result[:k]
    return result

if __name__ == "__main__":
    print(top_k_frequent([1,1,1,2,2,3], 2))  # [1,2]
    print(top_k_frequent([1], 1))              # [1]
