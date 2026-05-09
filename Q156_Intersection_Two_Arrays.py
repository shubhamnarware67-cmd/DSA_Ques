"""
Q156: Intersection of Two Arrays
==================================
Problem: Given two integer arrays, return their intersection.
Each element in result must be unique.

Example:
    [1,2,2,1], [2,2] -> [2]
    [4,9,5], [9,4,9,8,4] -> [9,4]
"""

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

def intersection_sorted(nums1, nums2):
    """Two-pointer approach after sorting"""
    nums1.sort(); nums2.sort()
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1; j += 1
        elif nums1[i] < nums2[j]: i += 1
        else: j += 1
    return result

if __name__ == "__main__":
    print(intersection([1,2,2,1], [2,2]))          # [2]
    print(intersection_sorted([4,9,5],[9,4,9,8,4])) # [4,9]
