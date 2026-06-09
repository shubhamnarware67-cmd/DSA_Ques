"""
Q270: Count of Range Sum (Merge Sort)
=======================================
Problem: Count number of range sums S(i,j) where lower<=S<=upper.
S(i,j)=nums[i]+...+nums[j].

Example:
    nums=[-2,5,-1], lower=-2, upper=2 -> 3
    (S(0,0)=-2, S(2,2)=-1, S(0,2)=2)
"""

def count_range_sum(nums, lower, upper):
    prefix = [0]
    for n in nums: prefix.append(prefix[-1] + n)
    count = [0]

    def merge_sort(arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        j = k = 0
        for l_val in left:
            while j < len(right) and right[j] - l_val < lower: j += 1
            while k < len(right) and right[k] - l_val <= upper: k += 1
            count[0] += k - j
        merged, l, r = [], 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]: merged.append(left[l]); l+=1
            else: merged.append(right[r]); r+=1
        merged.extend(left[l:]); merged.extend(right[r:])
        return merged

    merge_sort(prefix)
    return count[0]

if __name__ == "__main__":
    print(count_range_sum([-2,5,-1], -2, 2))  # 3
    print(count_range_sum([0], 0, 0))          # 1
