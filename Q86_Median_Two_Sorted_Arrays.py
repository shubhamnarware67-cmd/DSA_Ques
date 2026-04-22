"""
Q86: Median of Two Sorted Arrays (Binary Search)
=================================================
Problem: Given two sorted arrays of size m and n, find the median.
Must be O(log(m+n)).

Example:
    [1,3], [2]     -> 2.0
    [1,2], [3,4]   -> 2.5
"""

def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        max_left1 = float('-inf') if i == 0 else nums1[i-1]
        min_right1 = float('inf') if i == m else nums1[i]
        max_left2 = float('-inf') if j == 0 else nums2[j-1]
        min_right2 = float('inf') if j == n else nums2[j]
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 1:
                return float(max(max_left1, max_left2))
            return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
        elif max_left1 > min_right2:
            right = i - 1
        else:
            left = i + 1

if __name__ == "__main__":
    print(find_median_sorted_arrays([1,3], [2]))     # 2.0
    print(find_median_sorted_arrays([1,2], [3,4]))   # 2.5
