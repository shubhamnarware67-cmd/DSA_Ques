"""
Q332: Split Array Largest Sum (Binary Search + Greedy / DP)
=============================================================
Problem: Split array into m non-empty parts, minimize the largest sum.

Example:
    nums=[7,2,5,10,8], m=2 -> 18
    nums=[1,2,3,4,5], m=2  -> 9
"""

def split_array(nums, m):
    def can_split(mid):
        count = 1
        curr = 0
        for num in nums:
            if curr + num > mid:
                count += 1
                curr = 0
            curr += num
        return count <= m

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split(mid): hi = mid
        else: lo = mid + 1
    return lo

if __name__ == "__main__":
    print(split_array([7,2,5,10,8], 2))  # 18
    print(split_array([1,2,3,4,5], 2))   # 9
    print(split_array([1,4,4], 3))        # 4
