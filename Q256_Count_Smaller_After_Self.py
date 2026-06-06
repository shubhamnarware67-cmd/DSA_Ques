"""
Q256: Count of Smaller Numbers After Self (Merge Sort / BIT)
=============================================================
Problem: For each element, count how many elements to its right are smaller.

Example:
    [5,2,6,1] -> [2,1,1,0]
    [1]        -> [0]
    [-1,-1]    -> [0,0]
"""

def count_smaller(nums):
    result = [0] * len(nums)
    def merge_sort(indices):
        if len(indices) <= 1: return indices
        mid = len(indices) // 2
        left = merge_sort(indices[:mid])
        right = merge_sort(indices[mid:])
        merged = []
        l = r = 0
        while l < len(left) and r < len(right):
            if nums[left[l]] <= nums[right[r]]:
                result[left[l]] += r
                merged.append(left[l]); l += 1
            else:
                merged.append(right[r]); r += 1
        while l < len(left):
            result[left[l]] += r
            merged.append(left[l]); l += 1
        merged.extend(right[r:])
        return merged
    merge_sort(list(range(len(nums))))
    return result

if __name__ == "__main__":
    print(count_smaller([5,2,6,1]))  # [2,1,1,0]
    print(count_smaller([-1,-1]))    # [0,0]
    print(count_smaller([1]))        # [0]
