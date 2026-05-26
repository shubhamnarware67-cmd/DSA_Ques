"""
Q206: Next Greater Element I (Monotonic Stack)
===============================================
Problem: For each element in nums1, find next greater element in nums2.
Return -1 if none.

Example:
    nums1=[4,1,2], nums2=[1,3,4,2] -> [-1,3,-1]
    nums1=[2,4],   nums2=[1,2,3,4] -> [3,-1]
"""

def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    while stack:
        next_greater[stack.pop()] = -1
    return [next_greater[n] for n in nums1]

if __name__ == "__main__":
    print(next_greater_element([4,1,2],[1,3,4,2]))  # [-1,3,-1]
    print(next_greater_element([2,4],[1,2,3,4]))    # [3,-1]
