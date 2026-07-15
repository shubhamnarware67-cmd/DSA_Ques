"""
Q408: Sum of Subarray Minimums (Monotonic Stack)
=================================================
Problem: Find sum of min(b) over every subarray b of arr. Mod 10^9+7.

Example:
    [3,1,2,4] -> 17
    [11,81,94,43,3] -> 444
"""

def sum_subarray_mins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    stack = []
    result = 0
    for i in range(n + 1):
        while stack and (i == n or arr[stack[-1]] >= arr[i]):
            mid = stack.pop()
            left = stack[-1] if stack else -1
            right = i
            count = (mid - left) * (right - mid)
            result = (result + arr[mid] * count) % MOD
        stack.append(i)
    return result

if __name__ == "__main__":
    print(sum_subarray_mins([3,1,2,4]))        # 17
    print(sum_subarray_mins([11,81,94,43,3]))  # 444
