"""
Q371: Number of Arithmetic Triplets (Two Sum variant)
======================================================
Problem: Count triplets (i,j,k) where i<j<k and nums[j]-nums[i]==nums[k]-nums[j]==diff.

Example:
    nums=[0,1,4,6,7,10], diff=3 -> 2  ((0,4,7) and (1,4,7)? No: (0,3,6)? 
    Actually indices where nums are 0-based: (0,1,3) -> 0,1 diff=1? diff=3
    So: 0→1→4? 4-1=3, 1-0=1. No. 1→4→7: 4-1=3,7-4=3 ✓; 4→7→10: 7-4=3,10-7=3 ✓ -> 2
"""

def arithmetic_triplets(nums, diff):
    num_set = set(nums)
    count = 0
    for num in nums:
        if num + diff in num_set and num + 2*diff in num_set:
            count += 1
    return count

if __name__ == "__main__":
    print(arithmetic_triplets([0,1,4,6,7,10], 3))  # 2
    print(arithmetic_triplets([4,5,6,7,8,9], 2))   # 2
