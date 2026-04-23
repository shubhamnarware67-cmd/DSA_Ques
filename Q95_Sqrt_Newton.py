"""
Q95: Square Root using Newton's Method
========================================
Problem: Compute square root of a number using Newton-Raphson iteration.
More accurate than binary search for floating point.

Example:
    sqrt(25)   -> 5.0
    sqrt(2)    -> 1.41421356...
"""

def sqrt_newton(n, precision=1e-10):
    if n < 0:
        raise ValueError("Cannot take sqrt of negative number")
    if n == 0:
        return 0.0
    x = n
    while True:
        x_new = (x + n / x) / 2
        if abs(x_new - x) < precision:
            return x_new
        x = x_new

if __name__ == "__main__":
    print(f"sqrt(25) = {sqrt_newton(25)}")  # 5.0
    print(f"sqrt(2)  = {sqrt_newton(2):.10f}")  # 1.4142135624
    print(f"sqrt(9)  = {sqrt_newton(9)}")  # 3.0
