"""
Q142: Summary Ranges
=====================
Problem: Given sorted unique integer array, return smallest sorted list
of ranges that cover all numbers. "a->b" or "a".

Example:
    [0,1,2,4,5,7]   -> ["0->2","4->5","7"]
    [0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]
"""

def summary_ranges(nums):
    result = []
    i = 0
    while i < len(nums):
        start = nums[i]
        while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
            i += 1
        if nums[i] == start:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[i]}")
        i += 1
    return result

if __name__ == "__main__":
    print(summary_ranges([0,1,2,4,5,7]))    # ["0->2","4->5","7"]
    print(summary_ranges([0,2,3,4,6,8,9]))  # ["0","2->4","6","8->9"]
