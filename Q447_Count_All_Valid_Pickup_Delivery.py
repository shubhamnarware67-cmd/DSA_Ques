"""
Q447: Count All Valid Pickup and Delivery Options (Combinatorics)
====================================================================
Problem: n orders, each has pickup(i) and delivery(i). pickup(i) must come
before delivery(i). Count valid permutations mod 10^9+7.

Example:
    n=1 -> 1
    n=2 -> 6
    n=3 -> 90
"""

def count_orders(n):
    MOD = 10**9 + 7
    result = 1
    for i in range(1, n+1):
        # i-th order: (2i-1) slots for pickup, then (2i) slots total possible for delivery
        result = result * i * (2*i - 1) % MOD
    return result

if __name__ == "__main__":
    print(count_orders(1))  # 1
    print(count_orders(2))  # 6
    print(count_orders(3))  # 90
