"""
Q409: Sum of Subarray Ranges (Monotonic Stack)
===============================================
Problem: Range of subarray = max - min. Sum of ranges of all subarrays.

Example:
    [1,2,3] -> 4
    [1,3,3] -> 4
    [4,-2,-3,4,1] -> 59
"""

def sub_array_ranges(nums):
    def helper(arr):
        n, stack, result = len(arr), [], 0
        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                result += arr[mid] * (mid - left) * (i - mid)
            stack.append(i)
        return result

    return helper([-x for x in nums]) - helper(nums)

if __name__ == "__main__":
    print(sub_array_ranges([1,2,3]))         # 4
    print(sub_array_ranges([1,3,3]))         # 4
    print(sub_array_ranges([4,-2,-3,4,1]))   # 59
