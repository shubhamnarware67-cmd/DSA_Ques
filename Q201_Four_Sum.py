"""
Q201: 4Sum
===========
Problem: Given array and target, find all unique quadruplets that sum to target.

Example:
    nums=[1,0,-1,0,-2,2], target=0
    -> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

def four_sum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]: continue
            left, right = j+1, n-1
            while left < right:
                s = nums[i]+nums[j]+nums[left]+nums[right]
                if s == target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    while left < right and nums[left]==nums[left+1]: left+=1
                    while left < right and nums[right]==nums[right-1]: right-=1
                    left+=1; right-=1
                elif s < target: left+=1
                else: right-=1
    return result

if __name__ == "__main__":
    print(four_sum([1,0,-1,0,-2,2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    print(four_sum([2,2,2,2,2], 8))       # [[2,2,2,2]]
