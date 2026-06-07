"""
Q261: Partition to K Equal Sum Subsets (Backtracking + Bitmask)
================================================================
Problem: Given array and k, determine if we can divide it into k non-empty
subsets with equal sum.

Example:
    nums=[4,3,2,3,5,2,1], k=4 -> True  (subsets: {5},{1,4},{2,3},{2,3})
    nums=[1,2,3,4], k=3        -> False
"""

def can_partition_k_subsets(nums, k):
    total = sum(nums)
    if total % k != 0: return False
    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target: return False
    n = len(nums)
    dp = {}

    def backtrack(mask, cur_sum):
        if mask == (1<<n)-1: return True
        if (mask, cur_sum) in dp: return dp[(mask, cur_sum)]
        for i in range(n):
            if mask & (1<<i): continue
            if cur_sum + nums[i] <= target:
                new_sum = (cur_sum + nums[i]) % target
                if backtrack(mask | (1<<i), new_sum):
                    dp[(mask, cur_sum)] = True
                    return True
        dp[(mask, cur_sum)] = False
        return False

    return backtrack(0, 0)

if __name__ == "__main__":
    print(can_partition_k_subsets([4,3,2,3,5,2,1], 4))  # True
    print(can_partition_k_subsets([1,2,3,4], 3))          # False
