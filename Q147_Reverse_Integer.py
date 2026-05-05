"""
Q147: Reverse Integer
======================
Problem: Given 32-bit signed integer x, return x with its digits reversed.
If result overflows 32-bit signed integer, return 0.

Example:
    123   -> 321
    -123  -> -321
    120   -> 21
"""

def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_x = int(str(x_abs)[::-1])
    result = sign * reversed_x
    if result > INT_MAX or result < INT_MIN:
        return 0
    return result

if __name__ == "__main__":
    print(reverse(123))   # 321
    print(reverse(-123))  # -321
    print(reverse(120))   # 21
    print(reverse(1534236469))  # 0 (overflow)
