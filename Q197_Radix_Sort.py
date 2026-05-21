"""
Q197: Radix Sort
=================
Problem: Implement Radix Sort — sort integers digit by digit.
Time: O(d*(n+k)) where d=digits, k=10. Stable, non-comparative.

Example:
    [170,45,75,90,802,24,2,66] -> [2,24,45,66,75,90,170,802]
"""

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

if __name__ == "__main__":
    arr = [170,45,75,90,802,24,2,66]
    print(radix_sort(arr))  # [2,24,45,66,75,90,170,802]
