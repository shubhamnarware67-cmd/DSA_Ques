"""
Q266: Patching Array (Greedy)
==============================
Problem: Given sorted array and n, find minimum patches (numbers) to add
so every integer in [1,n] can be formed as sum of elements.

Example:
    nums=[1,3], n=6   -> 1  (add 2: now [1,2,3] covers 1-6)
    nums=[1,5,10], n=20 -> 2
    nums=[1,2,2], n=5 -> 0
"""

def min_patches(nums, n):
    patches = 0
    miss = 1  # Smallest missing reachable number
    i = 0
    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            miss += miss  # Patch with 'miss' itself doubles reach
            patches += 1
    return patches

if __name__ == "__main__":
    print(min_patches([1,3], 6))       # 1
    print(min_patches([1,5,10], 20))   # 2
    print(min_patches([1,2,2], 5))     # 0
