"""
Q333: Find K Closest Elements (Binary Search)
===============================================
Problem: Given sorted array, find k closest elements to x.
Return them sorted.

Example:
    arr=[1,2,3,4,5], k=4, x=3 -> [1,2,3,4]
    arr=[1,2,3,4,5], k=4, x=-1 -> [1,2,3,4]
"""
import bisect

def find_closest_elements(arr, k, x):
    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = (lo + hi) // 2
        # Compare distances of arr[mid] vs arr[mid+k] from x
        if x - arr[mid] > arr[mid+k] - x:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo+k]

if __name__ == "__main__":
    print(find_closest_elements([1,2,3,4,5], 4, 3))   # [1,2,3,4]
    print(find_closest_elements([1,2,3,4,5], 4, -1))  # [1,2,3,4]
    print(find_closest_elements([1,2,3,4,5], 4, 100)) # [2,3,4,5]
