"""
Q334: Kth Missing Positive Number (Binary Search)
===================================================
Problem: Given sorted array of positive integers, find kth missing positive.

Example:
    arr=[1,2,3,4], k=2   -> 6
    arr=[2,3,4,7,11], k=5 -> 9
"""

def find_kth_positive(arr, k):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # Number of missing positives up to arr[mid] = arr[mid] - (mid+1)
        if arr[mid] - (mid + 1) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo + k  # lo = position, k = kth missing after that

if __name__ == "__main__":
    print(find_kth_positive([1,2,3,4], 2))       # 6
    print(find_kth_positive([2,3,4,7,11], 5))    # 9
    print(find_kth_positive([1,2,3,4,5], 1))     # 6
