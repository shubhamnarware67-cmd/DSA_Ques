"""
Q257: Reverse Pairs (Merge Sort)
==================================
Problem: Count reverse pairs (i,j) where i<j and nums[i] > 2*nums[j].

Example:
    [1,3,2,3,1] -> 2
    [2,4,3,5,1] -> 3
"""

def reverse_pairs(nums):
    count = [0]
    def merge_sort(arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        j = 0
        for val in left:
            while j < len(right) and val > 2 * right[j]:
                j += 1
            count[0] += j
        merged, l, r = [], 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]: merged.append(left[l]); l+=1
            else: merged.append(right[r]); r+=1
        merged.extend(left[l:]); merged.extend(right[r:])
        return merged
    merge_sort(nums)
    return count[0]

if __name__ == "__main__":
    print(reverse_pairs([1,3,2,3,1]))  # 2
    print(reverse_pairs([2,4,3,5,1]))  # 3
