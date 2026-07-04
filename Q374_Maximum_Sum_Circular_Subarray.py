"""
Q374: Maximum Sum Circular Subarray (Kadane + Total Sum Trick)
==============================================================
Problem: Find max sum of subarray in circular array.
Either it's a normal subarray (Kadane's) or wraps around
(total sum - min subarray sum).

Example:
    [1,-2,3,-2] -> 3
    [5,-3,5]    -> 10
    [-3,-2,-3]  -> -2
"""

def max_subarray_sum_circular(nums):
    def kadane(arr):
        max_sum = cur = arr[0]
        for n in arr[1:]:
            cur = max(n, cur + n)
            max_sum = max(max_sum, cur)
        return max_sum

    total = sum(nums)
    max_normal = kadane(nums)
    max_wrapped = total - kadane([-n for n in nums])  # = total - min_subarray

    if max_wrapped == 0:  # All elements negative
        return max_normal
    return max(max_normal, max_wrapped)

if __name__ == "__main__":
    print(max_subarray_sum_circular([1,-2,3,-2]))  # 3
    print(max_subarray_sum_circular([5,-3,5]))      # 10
    print(max_subarray_sum_circular([-3,-2,-3]))    # -2
