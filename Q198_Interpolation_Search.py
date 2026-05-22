"""
Q198: Interpolation Search
============================
Problem: Like binary search but estimates position using interpolation.
Best for uniformly distributed sorted arrays.
Average: O(log log n), Worst: O(n)

Example:
    [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47], target=18 -> index 4
"""

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1
        # Estimate position
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

if __name__ == "__main__":
    arr = [10,12,13,16,18,19,20,21,22,23,24,33,35,42,47]
    print(interpolation_search(arr, 18))   # 4
    print(interpolation_search(arr, 33))   # 11
    print(interpolation_search(arr, 50))   # -1
