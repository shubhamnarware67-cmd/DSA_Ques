"""
Q340: Advanced Two Pointer Patterns
=====================================
Demonstrates 4 classic two-pointer problems:
1. Dutch Flag (3-way partition)
2. Partition Labels
3. Number of Subsequences
4. Boats to Save People

Example Q4: people=[1,2], limit=3 -> 1 boat
"""

# 1. Partition Labels
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result

# 2. Number of Subsequences
def num_subsequences(nums, target):
    MOD = 10**9 + 7
    nums.sort()
    n = len(nums)
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = pow2[i-1] * 2 % MOD
    lo, hi = 0, n-1
    count = 0
    while lo <= hi:
        if nums[lo] + nums[hi] <= target:
            count = (count + pow2[hi-lo]) % MOD
            lo += 1
        else:
            hi -= 1
    return count

# 3. Boats to Save People
def num_rescue_boats(people, limit):
    people.sort()
    lo, hi = 0, len(people)-1
    boats = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit: lo += 1
        hi -= 1
        boats += 1
    return boats

if __name__ == "__main__":
    print(partition_labels("ababcbacadefegdehijhklij"))  # [9,7,8]
    print(num_subsequences([3,5,6,7], 9))   # 4
    print(num_rescue_boats([1,2], 3))        # 1
    print(num_rescue_boats([3,2,2,1], 3))    # 3
