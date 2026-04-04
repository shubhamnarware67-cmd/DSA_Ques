"""
Q7: Merge Two Sorted Arrays
============================
Problem: Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array (in-place).

Example:
    Input: nums1 = [1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
    Output: [1,2,2,3,5,6]
"""

def merge(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    merge(nums1, 3, [2,5,6], 3)
    print(nums1)  # [1,2,2,3,5,6]
