"""
Q60: Integer Square Root (Binary Search)
=========================================
Problem: Given non-negative integer x, return integer square root
(floor value). Do not use built-in sqrt.

Example:
    4  -> 2
    8  -> 2  (floor of 2.828...)
"""

def my_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

if __name__ == "__main__":
    print(my_sqrt(4))   # 2
    print(my_sqrt(8))   # 2
    print(my_sqrt(16))  # 4
