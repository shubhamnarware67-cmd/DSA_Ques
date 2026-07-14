"""
Q405: Count Good Triplets (Brute Force / Optimized)
======================================================
Problem: Count triplets (i,j,k) where i<j<k and
|arr[i]-arr[j]|<=a, |arr[j]-arr[k]|<=b, |arr[i]-arr[k]|<=c.

Example:
    arr=[3,0,1,1,9,7], a=7, b=2, c=3 -> 4
    arr=[1,1,2,2,3], a=0, b=0, c=1   -> 0
"""

def count_good_triplets(arr, a, b, c):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(arr[i] - arr[j]) > a: continue
            for k in range(j+1, n):
                if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                    count += 1
    return count

if __name__ == "__main__":
    print(count_good_triplets([3,0,1,1,9,7], 7, 2, 3))  # 4
    print(count_good_triplets([1,1,2,2,3], 0, 0, 1))     # 0
