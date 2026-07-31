"""
Q414: Sliding Subarray Beauty (Counting + Sliding Window)
==========================================================
Problem: Beauty of subarray = xth smallest if negative, else 0.
Find beauty for every subarray of size k.

Example:
    nums=[1,-1,-3,-2,3], k=3, x=2 -> [-1,-2,-2]
    nums=[-1,-2,-3,-4,-5], k=2, x=2 -> [-1,-2,-3,-4]
"""

def get_subarray_beauty(nums, k, x):
    count = [0] * 101  # offset for -50..50
    result = []
    for i in range(k):
        count[nums[i] + 50] += 1
    def find_xth_smallest():
        c = 0
        for v in range(50):  # only check negatives (0-49 maps to -50..-1)
            c += count[v]
            if c >= x: return v - 50
        return 0
    result.append(find_xth_smallest())
    for i in range(k, len(nums)):
        count[nums[i] + 50] += 1
        count[nums[i-k] + 50] -= 1
        result.append(find_xth_smallest())
    return result

if __name__ == "__main__":
    print(get_subarray_beauty([1,-1,-3,-2,3], 3, 2))   # [-1,-2,-2]
    print(get_subarray_beauty([-1,-2,-3,-4,-5], 2, 2)) # [-1,-2,-3,-4]
