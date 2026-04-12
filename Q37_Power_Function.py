"""
Q37: Power Function - Fast Exponentiation
==========================================
Problem: Implement pow(x, n) which calculates x raised to the power n.

Example:
    pow(2.0, 10)  -> 1024.0
    pow(2.1, 3)   -> 9.261...
    pow(2.0, -2)  -> 0.25
"""

def my_pow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x, n = 1/x, -n
    result = 1.0
    while n:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

if __name__ == "__main__":
    print(my_pow(2.0, 10))   # 1024.0
    print(my_pow(2.1, 3))    # 9.261000000000001
    print(my_pow(2.0, -2))   # 0.25
