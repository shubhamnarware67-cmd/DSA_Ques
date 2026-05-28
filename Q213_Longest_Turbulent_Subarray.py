"""
Q213: Longest Turbulent Subarray (Sliding Window)
===================================================
Problem: Return length of maximum size turbulent subarray of nums.
Turbulent: alternates between > and < comparisons.

Example:
    [9,4,2,10,7,8,8,1,9] -> 5  ([4,2,10,7,8])
    [4,8,12,16]           -> 2
    [100]                  -> 1
"""

def max_turbulence_size(arr):
    n = len(arr)
    if n < 2: return n
    result = left = 1
    for right in range(1, n):
        if right == 1:
            if arr[right] != arr[right-1]: result = 2
            left = right - 1
        elif (arr[right] > arr[right-1]) != (arr[right-1] > arr[right-2]):
            result = max(result, right - left + 1)
        elif arr[right] == arr[right-1]:
            left = right
        else:
            left = right - 1
    return result

if __name__ == "__main__":
    print(max_turbulence_size([9,4,2,10,7,8,8,1,9]))  # 5
    print(max_turbulence_size([4,8,12,16]))             # 2
    print(max_turbulence_size([100]))                   # 1
