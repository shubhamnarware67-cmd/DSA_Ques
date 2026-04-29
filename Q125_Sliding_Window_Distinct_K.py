"""
Q125: Subarrays with K Different Integers (Sliding Window)
============================================================
Problem: Return number of subarrays with exactly k different integers.
Trick: exactly_k = at_most_k - at_most_(k-1)

Example:
    [1,2,1,2,3], k=2 -> 7
    [1,2,1,3,4], k=3 -> 3
"""
from collections import defaultdict

def subarrays_with_k_distinct(nums, k):
    def at_most(k):
        count = defaultdict(int)
        result = left = 0
        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            result += right - left + 1
        return result
    return at_most(k) - at_most(k - 1)

if __name__ == "__main__":
    print(subarrays_with_k_distinct([1,2,1,2,3], 2))  # 7
    print(subarrays_with_k_distinct([1,2,1,3,4], 3))  # 3
