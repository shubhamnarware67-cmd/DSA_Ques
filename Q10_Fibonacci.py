"""
Q10: Fibonacci Number
=====================
Problem: Given n, calculate F(n) where F(n) = F(n-1) + F(n-2),
with F(0) = 0 and F(1) = 1.

Example:
    Input: n = 10
    Output: 55
"""

def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive with memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

if __name__ == "__main__":
    print(fib(10))       # 55
    print(fib_memo(10))  # 55
    print([fib(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]
