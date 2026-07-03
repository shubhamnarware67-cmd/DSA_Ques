"""
Q369: Minimum Number of Platforms Required (Greedy / Two Pointers)
===================================================================
Problem: Given arrival and departure times, find minimum platforms needed
so no train waits.

Example:
    arr=[900,940,950,1100,1500,1800], dep=[910,1200,1120,1130,1900,2000] -> 3
"""

def minimum_platforms(arr, dep):
    arr.sort()
    dep.sort()
    n = len(arr)
    platforms = 1
    max_platforms = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)
    return max_platforms

if __name__ == "__main__":
    arr = [900,940,950,1100,1500,1800]
    dep = [910,1200,1120,1130,1900,2000]
    print(minimum_platforms(arr, dep))  # 3

    arr2 = [900,1100,1235]
    dep2 = [1000,1200,1240]
    print(minimum_platforms(arr2, dep2))  # 1
