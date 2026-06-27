"""
Q337: Count Special Quadruplets (HashMap)
==========================================
Problem: Count quadruplets (a,b,c,d) with a<b<c<d and nums[a]+nums[b]+nums[c]==nums[d].

Example:
    [1,2,3,6]       -> 1
    [3,3,6,4,5]     -> 0
    [1,1,1,3,5]     -> 4
"""
from collections import defaultdict

def count_quadruplets(nums):
    n = len(nums)
    count = 0
    # For each pair (b,c), look for d > c with nums[d] - nums[c] in map of nums[a] for a < b
    d_count = defaultdict(int)
    for c in range(n-2, 1, -1):
        d_count[nums[c+1]] += 1 if c == n-2 else 0
        # Add nums[c+1] when we first move c leftward
        for b in range(c-1, 0, -1):
            for a in range(b):
                need = nums[a] + nums[b] + nums[c]
                count += d_count[need]
    # Simpler O(n^3) approach:
    count2 = 0
    for a in range(n-3):
        for b in range(a+1, n-2):
            for c in range(b+1, n-1):
                for d in range(c+1, n):
                    if nums[a]+nums[b]+nums[c] == nums[d]:
                        count2 += 1
    return count2

if __name__ == "__main__":
    print(count_quadruplets([1,2,3,6]))     # 1
    print(count_quadruplets([3,3,6,4,5]))   # 0
    print(count_quadruplets([1,1,1,3,5]))   # 4
