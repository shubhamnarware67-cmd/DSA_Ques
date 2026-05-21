"""
Q196: Counting Sort
====================
Problem: Implement Counting Sort — efficient for small range integers.
Time: O(n+k), Space: O(k) where k = range of values.

Example:
    [4,2,2,8,3,3,1] -> [1,2,2,3,3,4,8]
    [1,0,3,1,3,1]   -> [0,1,1,1,3,3]
"""

def counting_sort(arr):
    if not arr: return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    result = []
    for i, cnt in enumerate(count):
        result.extend([i] * cnt)
    return result

def counting_sort_stable(arr):
    """Stable version preserving order of equal elements"""
    if not arr: return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr: count[num] += 1
    for i in range(1, len(count)): count[i] += count[i-1]
    result = [0] * len(arr)
    for num in reversed(arr):
        count[num] -= 1
        result[count[num]] = num
    return result

if __name__ == "__main__":
    print(counting_sort([4,2,2,8,3,3,1]))          # [1,2,2,3,3,4,8]
    print(counting_sort_stable([1,0,3,1,3,1]))     # [0,1,1,1,3,3]
